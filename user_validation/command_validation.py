import datetime


def date_validation(date):
    """
    Checks if the date is valid 
    
    Parameters:
        date (str): The date to be tested.
        
    Returns:
        bool: True if valid date, otherwise False.
    """
    try:
        yr,mm,dy = date.split('-')
        datetime.date(int(yr),int(mm),int(dy))
    except:
        return False
    return True


def time_validation(time):
    """
    Checks if the time is valid 
    
    Parameters:
        time (str): The time to be tested.
        
    Returns:
        bool: True if valid time, otherwise False.
    """
    try:
        hr,mm = time.split(':')
        datetime.time(int(hr),int(mm))
    except:
        return False
    return True


def check_for_normal_command(args):
    """
    Checks to see if the user's arguments are valid.
    Help commands are not considered.

    Parameters:
        args (list): User's arguments from command line input.

    Returns:
        bool: True if valid command, otherwise False.
    """

    len_two_args = ['my_calendar','booked_slots',
                    'my_volunteer_slots','open_slots']
    len_three_args = ['book_slot','cancel_booking','delete_slot']
    len_four_args = ['volunteer_slot']
    help_args = ['help','--help','-h']

    if len(args) == 2:
        if args[1] in len_two_args:
            return True
    elif len(args) == 3:
        if args[1] == len_two_args[0] and \
            (args[2].isdigit() or args[2] == 'iCal'):
            return True
        elif args[1] in len_three_args and args[2] not in help_args:
            return True
    elif len(args) == 4:
        if args[1] in len_four_args:
            return True
        elif args[1] == len_two_args[0] and \
            args[2].isdigit() and args[3] == 'iCal':
            return True

    return False


def check_for_help_command(args):
    """
    Checks for specific help commands.

    Parameters:
        args (list): User's arguments from command line input.

    Returns:
        bool: True if valid help command, otherwise False.
    """

    commands = ['my_calendar','booked_slots','my_volunteer_slots','open_slots',
                'book_slot','cancel_booking','delete_slot','volunteer_slot']
    help_commands = ['help','--help','-h']

    if len(args) == 3:
        if args[1] in commands and args[2] in help_commands:
            return True

    return False
