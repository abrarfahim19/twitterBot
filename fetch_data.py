# Dependencies
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API_URL key using os.getenv()
API_URL = os.getenv("API_URL")


# Fetch Price with API
def fetch_ethereum_price():
    try:
        # Make a request to the API
        response = requests.get(API_URL)

        if response.status_code == 200:
            data = response.json()
            ethereum_price = data["data"]["coin"]["price"]
            return ethereum_price
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
