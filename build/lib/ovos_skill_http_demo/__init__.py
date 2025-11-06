from ovos_workshop.skills import OVOSSkill
import requests


class HttpDemoSkill(OVOSSkill):
    def initialize(self):
        # This is a no-token-required API, so no need for settings here
        self.api_base = "https://jsonplaceholder.typicode.com"
        intent_path = self.find_resource("fetch_api.intent")
        if intent_path:
            self.log.info(f"Resolved fetch_api.intent path: {intent_path}")
        else:
            self.log.error("fetch_api.intent was not found in skill resources")
        self.register_intent_file("fetch_api.intent", self.handle_fetch_api)

    def handle_fetch_api(self, message):
        try:
            # API URL to fetch the post with ID 1
            url = f"{self.api_base}/posts/1"
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors

            # Parse the JSON response
            data = response.json()

            # Extract the title of the post (or any other data you like)
            result = data.get("title", "No title found")

            # Use a dialog file to speak the result
            self.speak_dialog("api_success", {"result": result})
        except requests.exceptions.RequestException:
            # If something goes wrong (network, API error, etc.)
            self.speak_dialog("api_error")

    def stop(self):
        return False


def create_skill(bus=None, skill_id=None, **kwargs):
    return HttpDemoSkill(bus=bus, skill_id=skill_id, **kwargs)
