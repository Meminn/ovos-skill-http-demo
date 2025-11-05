from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
import requests

class HttpDemoSkill(OVOSSkill):
    def initialize(self):
        # This is a no-token-required API, so no need for settings here
        self.api_base = "https://jsonplaceholder.typicode.com"

    @intent_handler('fetch.api.intent')  # Match this to the intent in your locale
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
            self.speak_dialog("api.success", {"result": result})
        except requests.exceptions.RequestException:
            # If something goes wrong (network, API error, etc.)
            self.speak_dialog("api.error")
            
    def stop(self):
        return False
