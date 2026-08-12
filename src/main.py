from api import get_events
from cli import parse_args
import commands

def main():
    try:
        args = parse_args()
        events = get_events(args.name)

        if len(args.params) > 1:
            raise ValueError("Only one parameter is allowed")
        
        commands.display_event(events, *args.params) 

    except ValueError as e:
        print(e)        

if __name__ == "__main__":
    main()