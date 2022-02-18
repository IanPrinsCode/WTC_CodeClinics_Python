import pickle
import os
def write_file(events_l):
    '''
    Writes user data to a file

    param:
        events_l: user events object
    '''
    if(os.path.exists("calendar_data/user_data.pickle")):
        with open("calendar_data/user_data.pickle", 'rb') as user_data:
            try:
                old_list = pickle.load(user_data)
            except:
                old_list = ''  #catch error for empty file
        if old_list != events_l:
            with open("calendar_data/user_data.pickle", 'wb') as user_data:
                pickle.dump(events_l, user_data)
    else:
        with open('calendar_data/user_data.pickle', 'wb') as user_data:
            pickle.dump(events_l, user_data)


def read_file():
    """
    This functions reads the contents of the user_data.pickle file
    and returns the contents. The return value is a list of all the
    upcoming events in the user's calendar.
    """
    try:
        with open("calendar_data/user_data.pickle", 'rb') as data:
            events = pickle.load(data)
        return events
    except:
        print("Your events could not be retrieved!")

