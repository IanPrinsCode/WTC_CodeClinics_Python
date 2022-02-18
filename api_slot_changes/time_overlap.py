import pytz
from datetime import datetime, timedelta


def check_personal_calendar_overlap(service, proposed_date, proposed_time):
    """
    Accesses the personal calendar's events and checks
    to see if the user's proposed date conflicts with
    any other events.

    Parameters:
        service (obj): Personal login credentials.
        proposed_date (str): The date that the slot will start.
        proposed_time (str): The time that the slot will start.

    Returns:
        bool: False if the time does not overlap and the time slot can be made,
                otherwise True.
    """

    page_token = None

    date_list = proposed_date.split('-')
    time_list = proposed_time.split(':')
    yr, mth, dy = int(date_list[0]), int(date_list[1]), int(date_list[2])
    hr, mn = int(time_list[0]), int(time_list[1])
    before_blockage = datetime(year=yr, month=mth, day=dy, hour=hr, minute=mn)
    before = before_blockage.astimezone(pytz.timezone('Africa/Johannesburg'))
    after = before + timedelta(minutes = 30)

    current = f"{str(before)[:10]}T{str(before)[11:19]}+02:00"
    after_str = f"{str(after)[:10]}T{str(after)[11:19]}+02:00"

    while True:
        events = service.events().list(calendarId='primary', timeMin=current,
                                        timeMax=after_str, singleEvents=True,
                                        orderBy='startTime').execute()

        if events['items'] != []:
            return True

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return False
