import datetime
import subprocess
import re
import os

def verify_user_credentials(user_email):
    """
    verify_user_credentials() will check whether the user
    attempting a log in is the same user who created the
    local copy of the token in the home directory.
    """
    email = input("Enter your student email address: ")

    if email == user_email:
        return True
    else: 
        return False


def check_token_exists():
    """
    check_token_exists() will check whether the auth token
    created for the user exists. If it does it will return
    True, else False.
    """
    # Check whether the token exists.
    if not os.path.isfile('{}/.token.pickle'.format(get_home_directory())):
        return False
    else:
        return True


def token_time_valid():
    """
    token_time_valid() checks whether the user's login window has expired.
    
    1. It creates a 3 hour time window as the login session.
    2. It checks if the user token was last modified within the 3 hour window.
    3. If the token was last modified within the 3 hour timeframe, it
       returns True.
    4. If the token was not modified, or if the token does not exist, 
       it returns False.
    """
    # Check the current time and create 3 hour timeout window.
    current_time = datetime.datetime.now()
    session = datetime.timedelta(hours=3)
    session_timeout = current_time - session


    # Get the time the token file was last modified.
    pickle_str = 'stat {}/.token.pickle'.format(get_home_directory())
    proc = subprocess.Popen(pickle_str, shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    str_output = str(output)[2:]
    mod_index = re.search('Modify:', str_output)
    index = mod_index.start()
    modify_time = str(output)[index + 10:index + 29]
    modified = datetime.datetime.strptime(modify_time, '%Y-%m-%d %H:%M:%S')

    if session_timeout < modified:
        # This condition indicates that the token was 
        # modified within the last 3 hours.
        return True
    else:
        # This condition indicates that the token was
        # modified more than 3 hours ago.
        return False


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


def update_token():
    """
    update_token() updates the time a file was modified,
    replacing the modification time with the current time.
    """
    os.system("touch -m {}/.token.pickle".format(get_home_directory()))


def do_logout():
    """
    Logs the user out by deleting their token, if it is found.

    No parameters.

    Returns None.
    """
    if os.path.exists(get_home_directory() + "/.token.pickle"):
        os.remove(get_home_directory() + "/.token.pickle")
