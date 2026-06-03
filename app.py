import json
import os
from datetime import datetime

DATA_FILE = 'schedule.json'

def load_schedule():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_schedule(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=2)

def add_event(title, date_time):
    events = load_schedule()
    events.append({"title": title, "datetime": date_time})
    save_schedule(events)
    print("Event added.")

def view_events():
    events = load_schedule()
    events.sort(key=lambda e: e["datetime"])
    for event in events:
        print(f"{event['datetime']} - {event['title']}")

def delete_event(index):
    events = load_schedule()
    if 0 <= index < len(events):
        deleted = events.pop(index)
        save_schedule(events)
        print(f"Deleted: {deleted['title']}")
    else:
        print("Invalid index.")

def main():
    while True:
        print("\n1. View Events\n2. Add Event\n3. Delete Event\n4. Exit")
        choice = input("Select: ")
        if choice == '1':
            view_events()
        elif choice == '2':
            title = input("Event Title: ")
            dt = input("Date & Time (YYYY-MM-DD HH:MM): ")
            try:
                datetime.strptime(dt, "%Y-%m-%d %H:%M")
                add_event(title, dt)
            except ValueError:
                print("Invalid date format.")
        elif choice == '3':
            view_events()
            idx = int(input("Event index to delete: "))
            delete_event(idx)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
