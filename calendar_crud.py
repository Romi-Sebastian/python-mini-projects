from datetime import datetime

events = []


def parse_datetime(prompt):
    while True:
        user_input = input(prompt + " (YYYY-MM-DD HH:MM): ")
        try:
            return datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format. Try again.")


def is_overlapping(new_start, new_end, skip_index=None):
    for i, event in enumerate(events):
        if i == skip_index:
            continue
        existing_start = event['start']
        existing_end = event['end']

        if new_start < existing_end and new_end > existing_start:
            return True
    return False


def add_event():
    title = input("Enter event title: ")
    start = parse_datetime("Start time")
    end = parse_datetime("End time")

    if start >= end:
        print("End time must be greater than start time")
        return

    if is_overlapping(start, end):
        print("This event overlaps with an existing one")
        return

    events.append({'title': title, 'start': start, 'end': end})
    print("Event added!")


def update_event():
    view_events()
    try:
        index = int(input("Enter the index of the event to update")) - 1
        if index not in range(len(events)):
            print("Invalid event number.")
            return
    except ValueError:
        print("Invalid input")
        return

    title = input("Enter new title(leave blank to keep current): ")
    start = parse_datetime("New start time")
    end = parse_datetime("New end time")

    if start >= end:
        print("End must be after start time")
        return

    if is_overlapping(start, end, skip_index=index):
        print("This update would cause an overlap.")
        return

    if title:
        events[index]['title'] = title
    events[index]['start'] = start
    events[index]['end'] = end
    print("Event updated")


def delete_event():
    view_events()
    try:
        index = int(input("Enter the index of the event to delete: ")) - 1
        if index in range(len(events)):
            removed = events.pop(index)
            print(f"Delete event: {removed['title']}")
        else:
            print("Invalid event number")
    except ValueError:
        print("Invalid input")


def view_events():
    if not events:
        print("No events.")
        return
    print("\n Scheduled Events:")
    for i, event in enumerate(sorted(events, key=lambda e: e['start']), start=1):
        print(f"{i}. {event['title']}")
        print(f"{event['start'].strftime('%Y-%m-%d %H:%M')} → {event['end'].strftime('%Y-%m-%d %H:%M')}")


def main():
    while True:
        print("\nCalender App")
        print("1. Add Event")
        print("2. Update Event")
        print("3. Delete Event")
        print("4. View All Events")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_event()
        elif choice == '2':
            update_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            view_events()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()