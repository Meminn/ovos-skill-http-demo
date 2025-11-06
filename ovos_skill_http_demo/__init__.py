from ovos_workshop.skills import OVOSSkill
import requests
class HttpDemoSkill(OVOSSkill):
    def initialize(self):
        # This is a no-token-required API, so no need for settings here
        # self.api_base = "https://jsonplaceholder.typicode.com"
        self.api_base = "https://localhost:3000/prompt"

        intent_path = self.find_resource("fetch_api.intent")
        if intent_path:
            self.log.info(f"Resolved fetch_api.intent path: {intent_path}")
        else:
            self.log.error("fetch_api.intent was not found in skill resources")
        self.register_intent_file("fetch_api.intent", self.handle_fetch_api)

    def handle_fetch_api(self, message):
        try:
            # Grab the raw utterance triggering this intent
            utterance = message.data.get("utterance")
            if not utterance:
                utterances = message.data.get("utterances") or []
                utterance = utterances[0] if isinstance(utterances, (list, tuple)) and utterances else ""

            payload = {"prompt": utterance}
            self.log.info(f"POST {self.api_base} payload={payload}")

            response = requests.post(
                self.api_base,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=15,
            )
            response.raise_for_status()  # Check for request errors

            # Parse the JSON response
            try:
                data = response.json()
            except ValueError:
                data = {"result": response.text.strip()}

            result = (
                data.get("result")
                or data.get("response")
                or data.get("text")
                or str(data)
            )

            self.log.info(f"API response: {result}")

            # Use a dialog file to speak the result
            self.speak_dialog("api_success", {"result": result})
        except requests.exceptions.RequestException as exc:
            self.log.exception(f"API request failed: {exc}")
            # If something goes wrong (network, API error, etc.)
            self.speak_dialog("api_error")

    def stop(self):
        return False


def create_skill(bus=None, skill_id=None, **kwargs):
    return HttpDemoSkill(bus=bus, skill_id=skill_id, **kwargs)
