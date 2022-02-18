from installs import pip_installs
import sys
from help import help_main, help_specific
from api_list_events import api_function_filters, print_events
from authentication import auth
from api_slot_changes import api
from login import login
from user_validation import command_validation
from calendar_data import data
from write_ical_files.create_ical_file import create_ical_file

def create_services():
    """
    First: checks to see if the token exists, and creates a service if not.
    Second: if token time expired, checks to see if email is the same,
            updates token if yes.
    Third: else asks user to login
    Fourth: updates token if within the time frame

    No parameters.

    Returns:
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        service (obj): Personal login credentials.
        user_email (str): User's email address.
    """

    if not login.check_token_exists():
        service = auth.do_personal_auth()

    elif not login.token_time_valid():
        service = auth.do_personal_auth()
        user_email = auth.get_user_email(service)

        if login.verify_user_credentials(user_email):
            login.update_token()
        else:
            login.do_logout()
            service = auth.do_personal_auth()

    else:
        service = auth.do_personal_auth()

    clinic_service = auth.do_codeclinic_auth()
    user_email = auth.get_user_email(service)
    return clinic_service, service, user_email


def start_cc_cli(args):
    """
    Handles the main part of the program.

    Parameters:
    args (list): Contains the user command line arguments.

    Returns None.
    """

    if not command_validation.check_for_normal_command(args):
        if command_validation.check_for_help_command(args):
            help_specific.do_help_specific(args[1])
            return
        help_main.do_help()
        return

    clinic_service, service, user_email = create_services()

    if len(args) == 2:
        if args[1] == 'my_calendar':
            api_function_filters.list_my_calendar(service, 7)
            print_events.print_user_events(data.read_file())
        elif args[1] == 'booked_slots':
            api_function_filters.list_booked_slots(clinic_service, user_email)
        elif args[1] == 'my_volunteer_slots':
            api_function_filters.list_my_volunteer_slots(clinic_service,
                                                            user_email)
        elif args[1] == 'open_slots':
            api_function_filters.list_open_slots(clinic_service, user_email)

    elif len(args) == 3:
        if args[1] == 'my_calendar' and args[2].isdigit():
            api_function_filters.list_my_calendar(service, int(args[2]))
            print_events.print_user_events(data.read_file())
        elif args[1] == 'my_calendar' and args[2] == 'iCal':
            events = api_function_filters.list_my_calendar(service, 7)
            print_events.print_user_events(data.read_file())
            create_ical_file(events, user_email)
        elif args[1] == 'book_slot':
            api.book_event(service, clinic_service, user_email, args[2])
            api_function_filters.list_my_calendar(service, 7)
        elif args[1] == 'cancel_booking':
            api.cancel_booking(clinic_service, user_email, args[2])
            api_function_filters.list_my_calendar(service, 7)
        elif args[1] == 'delete_slot':
            api.delete_event(clinic_service, user_email, args[2])
            api_function_filters.list_my_calendar(service, 7)
    
    elif len(args) == 4:
        if args[1] == 'volunteer_slot':
            api.insert_event(service,clinic_service,user_email,args[2],args[3])
            api_function_filters.list_my_calendar(service, 7)
        elif args[1] == 'my_calendar' and \
                args[2].isdigit() and \
                args[3] == 'iCal':
            events = api_function_filters.list_my_calendar(service,
                                                            int(args[2]))
            print_events.print_user_events(data.read_file())
            create_ical_file(events, user_email)
    else:
        print('Something went wrong! Please contact Team 5 ASAP.')

    return


if __name__ == '__main__':
    args = sys.argv
    start_cc_cli(args)
