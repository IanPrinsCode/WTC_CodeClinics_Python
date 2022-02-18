import random
import pytz
from datetime import datetime


def create_custom_id(id_map):
    """
    Creates a three digit code that is not in the id_map already, and adds
    the API id along with the custom id to the map.

    Parameters:
        id_map (dict): All current custom ids.
        api_id (str): The API event identification needing a custom id.

    Returns:
        id_map (dict): All custom ids with the new custom id.
    """

    custom_ids_list = id_map.keys()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    alph_list = list(alph)

    while True:
        a = alph_list[random.randint(0,25)]
        b = str(random.randint(0,9))
        c = alph_list[random.randint(0,25)]
        new_id = a + b + c
        if new_id not in custom_ids_list:
            break

    return new_id


def update_id_map(events, id_map):
    for event in events['items']:
        id_map[event['description']] = event['id']
    return id_map


def get_id_map_api(clinic_service):
    """
    Obtains all Google Calendar API events from the Code Clinic email.
    Past events are disregarded.

    Parameters:
        clinic_service (obj): WeThinkCode_ clinic login credentials.

    Returns:
        id_map (dict): All current custom ids.
    """

    page_token = None
    id_map = {}
    now = datetime.now()

    # Reformatting to timezone-aware dateTime object
    cape_town_now = now.astimezone(pytz.timezone('Africa/Johannesburg'))
    cape_town_now = cape_town_now.replace(microsecond=0)
    now = f"{str(cape_town_now)[:10]}T{str(cape_town_now)[11:19]}+02:00"
                         
    while True:
        events = clinic_service.events().list(calendarId='primary',
                                        timeMin=now,
                                        singleEvents=True,
                                        orderBy='startTime').execute()

        id_map = update_id_map(events, id_map)

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return id_map


def convert_custom_id_to_api_id(clinic_service, custom_id):
    id_map = get_id_map_api(clinic_service)
    try:
        api_id = id_map[custom_id]
    except:
        return ''
    else:
        return api_id
