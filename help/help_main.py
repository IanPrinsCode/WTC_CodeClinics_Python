from rich import print


def do_help():
    print("""
[bold blue]WTC_ code clinic has the following command-line tools:[/bold blue]
[bold blue]*[/bold blue] run 'python3 code_clinics.py' with a following command to use it.
[bold blue]    ex.[/bold blue] python3 code_clinics.py booked_slots
[bold blue]*[/bold blue] optional arguments are displayed in [yellow]<>[/yellow] brackets.
[bold blue]*[/bold blue] required arguments are displayed in [red]<>[/red] brackets.

Viewings of Calendars:
        [green]my_calendar[/green] [yellow]<number>[/yellow] [yellow]<iCal>[/yellow]
        [green]booked_slots[/green]
        [green]my_volunteer_slots[/green]
        [green]open_slots[/green]

Booking System:
    [green]book_slot[/green] [red]<event_id>[/red]
    [green]cancel_booking[/green] [red]<event_id>[/red]

Volunteer System:
    [green]volunteer_slot[/green] [red]<date> <time>[/red]
    [green]delete_slot[/green] [red]<event_id>[/red]

[bold blue]Note:
*[/bold blue] Add 'help', '--help', or '-h' after a [green]basic command[/green] to get that specific help menu.
[bold blue]    ex.[/bold blue] python3 code_clinics.py my_calendar --help""")
