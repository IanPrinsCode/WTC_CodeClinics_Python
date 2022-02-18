from custom_id import custom_id
from datetime import datetime
from api_slot_changes import time_overlap
import user_validation.command_validation as uv

def insert_event(service, clinic_service, user_email, date, start_time):
    """
    Does an API call to create a volunteer event for the user.

    Parameters:
        service (obj): Personal login credentials.
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        user_email (str): email of logged in student.
        date (str): Receives date for event as input from user.
        start_time (str): Receives time for event as input from user.

    Returns:
        events (dict): Containing all personal calendar events.
    """

    if not uv.date_validation(date):
        print ('Invalid Date. Please enter in this format. yyyy-mm-dd')
        return
    elif not uv.time_validation(start_time):
        print ('Invalid Time. Please enter in this format. hh:mm')
        return

    yr,mm,dy = date.split('-')
    hr,mt = start_time.split(':')
    if datetime.now() > datetime(int(yr), int(mm), int(dy), int(hr), int(mt)):
        print('You can only book a date and time for the future.')
        return

    if time_overlap.check_personal_calendar_overlap(service, date, start_time):
        print('You cannot volunteer an event for that date and time!')
        m = 'Your personal calendar has at least one meeting that conflicts.'
        print(m)
        return

    if int(start_time[3:]) + 30 >=60:
        end_time = f"{int(start_time[:-3])+1}:{(int(start_time[3:])+30)-60}"
    else:
        end_time = f"{int(start_time[:-3])}:{(int(start_time[3:]) + 30)}"

    dateTime_start = f"{date}T{start_time}:00+02:00"
    dateTime_end = f"{date}T{end_time}:00+02:00"
    
    # Ask for event description
    i = """Please briefly specify what topic you are available to help with.
[ex. unit-tests, lambda expressions, etc.]
 -> """
    description = input(i).rstrip()
    id_map = custom_id.get_id_map_api(clinic_service)
    new_id = custom_id.create_custom_id(id_map)
    event = {
            'summary': 'Code Clinic: ' + description,
            'location': 'Google Meets',
            'description': new_id,
            'start': {
                      'dateTime': '{}'.format(dateTime_start),
                      'timeZone': 'Africa/Johannesburg',
                     },
            'end': {
                    'dateTime': '{}'.format(dateTime_end),
                    'timeZone': 'Africa/Johannesburg',
                   },
            'attendees': [
                          {'email': 'wethinkcode.codeclinic@gmail.com',
                            "owner": True,
                            "comment": "undercover FBI"},
                          {'email': '{}'.format(user_email),
                            "comment": "volunteer"}
                         ],
            'maxAttendees': 3,
            'reminders': {'useDefault': True},
            'guestsCanModify': False,
            'guestsCanInviteOthers': False,
            }
    
    event = clinic_service.events().insert(calendarId='primary',
                                            body=event).execute()
    print('You have successfully volunteered a slot.')

    return event


def delete_event(clinic_service, user_email, input_id):
    """
    Removes an unbooked event that you volunteered, using an API call.

    Parameters:
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        user_email (str): email of logged in student.
        input_id (str): ID of the event that is to be removed.

    Returns None.Z
    """

    event_id = custom_id.convert_custom_id_to_api_id(clinic_service, input_id)
    if event_id == '':
        print('That is not a valid event ID.')
        return

    event = clinic_service.events().get(calendarId='primary',
                                            eventId=event_id).execute()
    volunteer_name = ""
    
    for person in event['attendees']:
        if person['comment'] == 'volunteer':
            volunteer_name = person['email']
    if volunteer_name != user_email:
        print('This event does not belong to you. You cannot delete it.')
    elif len(event['attendees']) == 2:
        clinic_service.events().delete(calendarId='primary',
                                        eventId=event_id).execute()
        print('Your event has been succesfully deleted')
    else:
        m = 'This event has been booked already. You cannot delete the event.'
        print(m)


def book_event(service, clinic_service, user_email, input_id):
    """
    Books the user to a volunteered event if the event_id
    is correct, the volunteer is not the user, and if
    the event is not already booked.

    Parameters:
        clinic_service (obj): WeThinkCode_ clinic login credentials.
        user_email (str): The user's personal email name.
        event_id (str): The specific Google Calendar API event
                        identification code.

    Returns None.
    """

    event_id = custom_id.convert_custom_id_to_api_id(clinic_service, input_id)
    if event_id == '':
        print('That is not a valid event ID.')
        return

    event = clinic_service.events().get(calendarId='primary',
                                            eventId=event_id).execute()
    date = event['start']['dateTime'][:10]
    start_time = event['start']['dateTime'][11:16]

    volunteer_name = ""
    
    for person in event['attendees']:
        if person['comment'] == 'volunteer':
            volunteer_name = person['email']
    if volunteer_name == user_email:
        print('You can not book your own clinic slot!')
    elif len(event['attendees']) == 2:
        m = 'Your personal calendar has at least one meeting that conflicts.'
        if time_overlap.check_personal_calendar_overlap(service,
                                                            date, start_time):
            print('You cannot book this event because of the date and time!')
            print(m)
            return
        else:
            event['attendees'].append({'email': user_email,
                                        'comment': 'bookee'})
            u_event = clinic_service.events().update(calendarId='primary',
                                                        eventId=event['id'],
                                                        body=event).execute()
            s = 'summary'
            print('You have successfully booked {} event.'.format(u_event[s]))
    else:
        print('This slot is already booked!')


def cancel_booking(clinic_service, user_email, input_id):
    """
    Removes the booked client from their booked appointment
    if they are the ones who have booked the event_id slot.

    Parameters:
        clinic_service (obj): Clinic login credentials.
        user_email (str): The user's personal email name.
        event_id (str): The specific Google Calendar API event
                        identification code.

    Returns None.
    """

    event_id = custom_id.convert_custom_id_to_api_id(clinic_service, input_id)
    if event_id == '':
        print('That is not a valid event ID.')
        return

    event = clinic_service.events().get(calendarId='primary',
                                        eventId=event_id).execute()
    bookee_name = ""
    to_remove = None
    
    for person in event['attendees']:
        if person['comment'] == 'bookee':
            bookee_name = person['email']
    if len(event['attendees']) == 2:
        print('Event is not booked yet and can not be canceled!')
    elif bookee_name != user_email:
        print('You did not book this event.')
        print('You are not allowed to cancel the booking!')
    else:
        for person in event['attendees']:
            if person['email'] == user_email:
                to_remove = person
        if to_remove in event['attendees']:
            event['attendees'].pop(event['attendees'].index(to_remove))
            print('You have successfully unsubscribed from that booking.')

    clinic_service.events().update(calendarId='primary',
                                    eventId=event['id'],
                                    body=event).execute()
