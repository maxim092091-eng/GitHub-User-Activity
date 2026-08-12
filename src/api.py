import requests, json

def get_events(username: str):
    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)
    response.raise_for_status()
    
    return response.json()
        