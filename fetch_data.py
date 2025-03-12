import requests
import json
import datetime
from subprocess import run

# Define the API URL and your API key
API_URL = "https://v3.football.api-sports.io/fixtures"
API_KEY = "e527606df5ab264030b3dd901fcf05c7"

# Function to fetch data from the API
def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Function to save data to a JSON file
def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Function to commit and push changes to the repository
def commit_and_push():
    run(["git", "add", "football.json"])
    run(["git", "commit", "-m", f"Updated feeds on {datetime.datetime.now()}"])
    run(["git", "push"])

# Main function
def main():
    headers = {
        "x-apisports-key": API_KEY,
        "Accept": "application/json"
    }
    football_data = fetch_data(API_URL, headers)

    if football_data:
        save_data(football_data, "football.json")
        commit_and_push()

if __name__ == "__main__":
    main()

