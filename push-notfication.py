import http.client
import urllib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Pushover credentials
APP_TOKEN = os.getenv("APP_TOKEN")
USER_KEY = os.getenv("USER_KEY")

# Custom message to send to your device
message = "hello world"

# Pushover notification request
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
urllib.parse.urlencode({
    "token": APP_TOKEN,
    "user": USER_KEY,
    "message": message,
}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
