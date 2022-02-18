import sys
if 'tests/test_help.py' not in sys.argv:    
    from rich import print

# command = (input("Command: "))

def do_help_specific(command):
    """
    do_help_command() takes a command as input.
    Depending on the command, it displays help
    information for that command.
    """
    if command == 'my_calendar':
        print("""
* optional arguments are displayed in [yellow]<>[/yellow] brackets.

[green]python3 code_clinics.py my_calendar[/green] [yellow]<number>[/yellow] [yellow]<iCal>[/yellow]
    
    - By default, it will display 7 days worth of events.
    - If you enter [yellow]<number>[/yellow] as a command-line argument, it will display events for that amount of days.
    - If you enter [yellow]<iCal>[/yellow] your events will be written to an iCal file and saved under your home directory.
    - If both optional arguments are used, the [yellow]<number>[/yellow] argument must precede the [yellow]<iCal>[/yellow] argument.\n""")

    elif command == 'booked_slots':
        print("""
[green]python3 code_clinics.py booked_slots[/green]

    - Displays all the upcoming code clinics you have subscribed to.\n""")

    elif command == 'my_volunteer_slots':
        print("""
[green]python3 code_clinics.py my_volunteer_slots[/green]

    - Displays all the slots you have volunteered.\n""")

    elif command == 'open_slots':
        print("""
[green]python3 code_clinics.py open_slots[/green]

    - Displays all the available Code Clinic slots.\n""")

    elif command == 'book_slot':
        print("""
* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py book_slot[/green] [red]<event_id>[/red]

    - Allows you to book a slot.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py open_slots[/italic]'[/white] and copying the eventID from the stdout.\n""")

    elif command == 'volunteer_slot':
        print("""
* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py volunteer_slot[/green] [red]<date> <time>[/red]

    - Allows you to volunteer a slot.
    - [red]<date>[/red] Must be in the format: yyyy-mm-dd   i.e. [blue]2020-01-01[/blue].
    - [red]<time>[/red] Must be in the format: hh:mm        i.e. [blue]12:00[/blue] (uses 24-hour format).\n""")

    elif command == 'cancel_booking':
        print("""
* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py cancel_booking[/green] [red]<event_id>[/red]

    - Allows you to cancel a booking for a code clinic.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py bookings[/italic]'[/white] and copying the eventID from stdout.\n""")

    elif command == 'delete_slot':
        print("""
* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py delete_slot[/green] [red]<event_id>[/red]

    - Deletes a slot if it has not been subscribed to.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py my_volunteer_slots[/italic]'[/white] and copying the eventID from stdout.\n""")
