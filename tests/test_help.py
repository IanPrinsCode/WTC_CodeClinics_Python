import unittest
import sys
import help.help_specific as hs
import help.help_main as hm
import tests.helper_functions as tb


class TestHelp(unittest.TestCase):

    def test_do_help(self):
        with tb.capture_output() as (out,err):
            hm.do_help()

        output = out.getvalue().strip()
        self.assertEqual(output, """WTC_ code clinic has the following command-line tools:
* run 'python3 code_clinics.py' with a following command to use it.
    ex. python3 code_clinics.py booked_slots
* optional arguments are displayed in <> brackets.
* required arguments are displayed in <> brackets.

Viewings of Calendars:
        my_calendar <number> <iCal>
        booked_slots
        my_volunteer_slots
        open_slots

Booking System:
    book_slot <event_id>
    cancel_booking <event_id>

Volunteer System:
    volunteer_slot <date> <time>
    delete_slot <event_id>

Note:
* Add 'help', '--help', or '-h' after a basic command to get that specific help menu.
    ex. python3 code_clinics.py my_calendar --help""")

    def test_help_my_calendar(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('my_calendar')
        
        output = out.getvalue().strip()
        self.assertEqual(output, """* optional arguments are displayed in [yellow]<>[/yellow] brackets.

[green]python3 code_clinics.py my_calendar[/green] [yellow]<number>[/yellow] [yellow]<iCal>[/yellow]
    
    - By default, it will display 7 days worth of events.
    - If you enter [yellow]<number>[/yellow] as a command-line argument, it will display events for that amount of days.
    - If you enter [yellow]<iCal>[/yellow] your events will be written to an iCal file and saved under your home directory.
    - If both optional arguments are used, the [yellow]<number>[/yellow] argument must precede the [yellow]<iCal>[/yellow] argument.""")


    def test_help_booked_slots(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('booked_slots')
        
        output = out.getvalue().strip()
        
        self.assertEqual(output, """[green]python3 code_clinics.py booked_slots[/green]

    - Displays all the upcoming code clinics you have subscribed to.""")


    def test_help_my_volunteer_slots(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('my_volunteer_slots')
        
        output = out.getvalue().strip()
        
        self.assertEqual(output, """[green]python3 code_clinics.py my_volunteer_slots[/green]

    - Displays all the slots you have volunteered.""")


    def test_help_open_slots(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('open_slots')

        output = out.getvalue().strip()
            
        self.assertEqual(output, """[green]python3 code_clinics.py open_slots[/green]

    - Displays all the available Code Clinic slots.""")


    def test_help_book_slot(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('book_slot')
        
        output = out.getvalue().strip()
        
        self.assertEqual(output, """* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py book_slot[/green] [red]<event_id>[/red]

    - Allows you to book a slot.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py open_slots[/italic]'[/white] and copying the eventID from the stdout.""")


    def test_help_volunteer_slot(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('volunteer_slot')
            
        output = out.getvalue().strip()
        
        self.assertEqual(output, """* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py volunteer_slot[/green] [red]<date> <time>[/red]

    - Allows you to volunteer a slot.
    - [red]<date>[/red] Must be in the format: yyyy-mm-dd   i.e. [blue]2020-01-01[/blue].
    - [red]<time>[/red] Must be in the format: hh:mm        i.e. [blue]12:00[/blue] (uses 24-hour format).""")


    def test_help_cancel_booking(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('cancel_booking')
        
        output = out.getvalue().strip()
        
        self.assertEqual(output, """* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py cancel_booking[/green] [red]<event_id>[/red]

    - Allows you to cancel a booking for a code clinic.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py bookings[/italic]'[/white] and copying the eventID from stdout.""")


    def test_help_delete_slot(self):
        with tb.capture_output() as (out, err):
            hs.do_help_specific('delete_slot')
        
        output = out.getvalue().strip()
        
        self.assertEqual(output, """* required arguments are displayed in [red]<>[/red] brackets.

[green]python3 code_clinics.py delete_slot[/green] [red]<event_id>[/red]

    - Deletes a slot if it has not been subscribed to.
    - The [red]<event_id>[/red] for slots can be acquired by running [white]'[italic]python3 code_clinics.py my_volunteer_slots[/italic]'[/white] and copying the eventID from stdout.""")


if __name__ == '__main__':
    unittest.main()