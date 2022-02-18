import ics
import datetime
import subprocess
import os

def get_home_directory():
    """
    Returns the user's home directory as a string.

    No parameters.

    Returns:
        home_path (str): The location of the home directory.
    """

    proc = subprocess.Popen('echo $HOME', shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    home_path = str(output)[2:-3]
    return home_path


def create_ical_file(events, username):
    """
    create_ical_files() receives the user's email and the events
    object as parameters.
    1. It makes use of the python ics module the set up a calendar
       and event.
    2. It iterates over the events in the events object and uses
       the values it finds to create a copy of the event in ical
       format.
    3. For each event, it adds that event to the iCal calendar
       object.
    4. Once all the events have been added, it writes those
       events to an ics file. The file is written to the user's home 
       directory and is named according to the user's email 
       and the date on which it was created. 
    5. It will print out a notification so that the user
       knows where to find it.
    """

    cal = ics.Calendar()
    event = ics.Event()
    time = datetime.date.today()

    for item in events['items']:
        try:
            event.name = item['summary']
            event.begin = convert_time_format(item['start']['dateTime'])
            event.duration = datetime.timedelta(minutes=30)
            event.uid = item['id']
            attendees = []
            for person in item['attendees']:
                attendees.append(person['email'])
            event.attendees = attendees
            
            cal.events.add(event)
        except:
            continue

    m = "{}/code_clinic_ical_files".format(get_home_directory())
    if not os.path.isdir(m):
        os.mkdir("{}/code_clinic_ical_files".format(get_home_directory()))

    i = '{}/code_clinic_ical_files/{}: {}.ics'.format(get_home_directory(),
                                                        username, time)
    with open(i, 'w') as my_file:
        my_file.writelines(cal)

    print("Events written to iCal file.")
    print("Check the code_clinic_ical_files folder in your home directory")


def convert_time_format(timestamp):
    """
    convert_time_format() will take the time format for the google
    API event and convert it to the format for iCAl files.
    """

    # iCal time format = 2014-01-01 00:00:00

    date = timestamp[:10]
    time = timestamp[11:19]

    updated_timestamp = "{} {}".format(date, time)

    return updated_timestamp
