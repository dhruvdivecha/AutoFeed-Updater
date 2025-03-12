#!/usr/bin/env python3

import requests
import json
import datetime

# API URLs (Replace with actual API keys)
CRICKET_API_URL = "https://api.cricapi.com/v1/matches?apikey=YOUR_API_KEY"
FOOTBALL_API_URL = "https://v3.football.api-sports.io/e527606df5ab264030b3dd901fcf05c7"

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    cricket_data = fetch_data(CRICKET_API_URL)
    football_data = fetch_data(FOOTBALL_API_URL)

    if cricket_data:
        save_data(cricket_data, "cricket.json")
    if football_data:
        save_data(football_data, "football.json")

    # Commit changes
    commit_and_push()

def commit_and_push():
    from subprocess import run
    run(["git", "add", "cricket.json", "football.json"])
    run(["git", "commit", "-m", f"Updated feeds on {datetime.datetime.now()}"])
    run(["git", "push"])

if __name__ == "__main__":
    main()
