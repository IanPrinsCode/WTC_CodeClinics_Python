import pytz
from datetime import datetime, timedelta
from api_list_events.print_events import print_user_events
from calendar_data import data


def list_my_calendar(service, user_days):
    """
    Obtains the user's calendar events for a certain amount
    of days using the service object.

    Parameters:
        service (obj): Personal login credentials.
        user_days (int): The amount of days worth of events to be displayed.

    Returns:
        events (dict): Containing all personal calendar events.
    """
    page_token = None
    now = datetime.now()

    # Reformatting to timezone-aware dateTime object
    cape_town_now = now.astimezone(pytz.timezone('Africa/Johannesburg'))
    cape_town_now = cape_town_now.replace(microsecond=0)
    ct_week_later = cape_town_now + timedelta(days = user_days)
    now = f"{str(cape_town_now)[:10]}T{str(cape_town_now)[11:19]}+02:00"
    later = f"{str(ct_week_later)[:10]}T{str(ct_week_later)[11:19]}+02:00"

    while True:
        events = service.events().list(calendarId='primary', timeMin=now,
                                        timeMax=later, singleEvents=True,
                                        orderBy='startTime').execute()

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    data.write_file(events)
    return events


def list_booked_slots(service, user_email):
    """
    Makes a call to Google calendar API to receive an events dictionary.
    List of items in dictionary is filtered to contain all Code Clinic
    events that the user has booked.

    Parameters:
        service (obj): Personal login credentials.
        user_email (str): The user's personal email.

    Returns:
        events (dict): Dictionary containing all relevant events for the call.
    """
    page_token = None
    new_list = []
    now = datetime.now()

    cape_town_now = now.astimezone(pytz.timezone('Africa/Johannesburg'))
    cape_town_now = cape_town_now.replace(microsecond=0)
    now = f"{str(cape_town_now)[:10]}T{str(cape_town_now)[11:19]}+02:00"

    while True:
        events = service.events().list(calendarId='primary',
                                        singleEvents=True,
                                        timeMin=now,
                                        orderBy='startTime').execute()

        for event in events['items']:
            bookee_name = ''
            if 'attendees' in event.keys():
                if len(event['attendees']) == 3:
                    for person in event['attendees']:
                        if person['comment'] == 'bookee':
                            bookee_name = person['email']
            if bookee_name == user_email:
                new_list.append(event)

        events['items'] = new_list

        print_user_events(events)

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return events


def list_open_slots(clinic_service, user_email):
    """
    Makes a call to Google calendar API to receive an events dictionary.
    List of items in dictionary is filtered to contain all unbooked Code Clinic
    events that any users volunteered.

    Parameters:
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        user_email (str): The user's personal email.

    Returns:
        events (dict): Dictionary containing all relevant events for the call.
    """
    page_token = None
    viable_events = []
    volunteer_name = ''
    now = datetime.now()

    cape_town_now = now.astimezone(pytz.timezone('Africa/Johannesburg'))
    cape_town_now = cape_town_now.replace(microsecond=0)
    now = f"{str(cape_town_now)[:10]}T{str(cape_town_now)[11:19]}+02:00"

    while True:
        events = clinic_service.events().list(calendarId='primary',
                                        singleEvents=True,
                                        timeMin=now,
                                        orderBy='startTime').execute()

        for event in events['items']:
            if len(event['attendees']) == 2:
                for person in event['attendees']:
                    if person['comment'] == 'volunteer':
                        volunteer_name = person['email']
                if volunteer_name != user_email:
                    viable_events.append(event)
        events['items'] = viable_events

        print_user_events(events)

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return events


def list_my_volunteer_slots(clinic_service, user_email):
    """
    Makes a call to Google calendar API to receive an events dictionary.
    List of items in dictionary is filtered to only contain events that the
    user volunteered.

    Parameters:
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        user_email (str): The user's personal email.

    Returns:
        events (dict): Dictionary containing all relevant events for the call.
    """
    page_token = None
    viable_events = []
    volunteer_name = ''
    now = datetime.now()

    cape_town_now = now.astimezone(pytz.timezone('Africa/Johannesburg'))
    cape_town_now = cape_town_now.replace(microsecond=0)
    now = f"{str(cape_town_now)[:10]}T{str(cape_town_now)[11:19]}+02:00"

    while True:
        events = clinic_service.events().list(calendarId='primary',
                                        singleEvents=True,
                                        timeMin=now,
                                        orderBy='startTime').execute()

        for event in events['items']:
            for person in event['attendees']:
                if person['comment'] == 'volunteer':
                    volunteer_name = person['email']
            if volunteer_name == user_email:
                viable_events.append(event)
        events['items'] = viable_events

        print_user_events(events)

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return events
