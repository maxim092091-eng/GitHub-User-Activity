import requests

seen_events = set()
def display_event(events: dict, filter: str | None = None) -> None:
    there_event = False
    for event in events:
        type_event = event["type"]
        repo = event["repo"]["name"]
        if ((type_event, repo) not in seen_events
            and (filter is None or filter.title() in type_event)
            ):
            there_event = True 
            if type_event == "PushEvent":
                repo = event["repo"]["name"]
                before = event["payload"]["before"]
                head = event["payload"]["head"]

                url = f"https://api.github.com/repos/{repo}/compare/{before}...{head}"
                response = requests.get(url)

                commits = response.json()["total_commits"]

                print(f"Pushed {commits} commits to {repo}")

            elif type_event == "IssuesEvent":
                print(f"Opened a new issue in {repo}")
            
            elif type_event in [
                "CreateEvent", "DeleteEvent", 
                "GollumEvent", "PublicEvent", "PushEvent"
                ]:
                print(f"{type_event.removesuffix("Event").removesuffix("e")}ed {repo}")

            else:
                print(f"{event["payload"]["action"].title()} {repo}")

            seen_events.add((type_event, repo))

    if not there_event:
        print("There are no events")