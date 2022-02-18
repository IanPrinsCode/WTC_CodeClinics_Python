from __future__ import print_function
import subprocess
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_user_email(service):
    """
    This function will return the email address ascociated with
    the service.
    """
    calendar = service.calendars().get(calendarId='primary').execute()
    return calendar['id']


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


def do_codeclinic_auth():
    """
    do_codeclinic_auth() uses Google's OAuth 2.0 endpoints to authorize access
    to Google APIs.
    1. The user will be redirected to a browser window where they will
       log in to their google account and grant the program access to
       their google calendar.
    2. Google will respond by sending an access token, which is stored
       in a token file.
    3. The access token is used to create a service instance which
       allows the program to edit and read calendar events.
    4. It returns a service instance to be used by other parts of the
       program. 
    """
    # If modifying these scopes, delete the file .token.pickle.
    SCOPES = [
              'https://www.googleapis.com/auth/calendar.events',
              'https://www.googleapis.com/auth/calendar',
              'https://www.googleapis.com/auth/calendar.settings.readonly',
              'https://www.googleapis.com/auth/calendar.addons.execute'
             ]
    creds = None
    
    #The file .token.pickle stores the user's access and refresh tokens, and is
    #created automatically when the authorization flow completes for the first
    #time.

    if os.path.exists('authentication/.token.pickle'):
        with open('authentication/.token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.abspath('authentication/client_secret.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('authentication/.token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def do_personal_auth():
    """
    do_auth() uses Google's OAuth 2.0 endpoints to authorize access to 
    Google APIs.
    1. The user will be redirected to a browser window where they will
       log in to their google account and grant the program access to
       their google calendar.
    2. Google will respond by sending an access token, which is stored
       in a token file.
    3. The access token is used to create a service instance which
       allows the program to edit and read calendar events.
    4. It returns a service instance to be used by other parts of the
       program. 
    """
    # If modifying these scopes, delete the file .token.pickle.
    SCOPES = [
              'https://www.googleapis.com/auth/calendar.events',
              'https://www.googleapis.com/auth/calendar',
              'https://www.googleapis.com/auth/calendar.settings.readonly',
              'https://www.googleapis.com/auth/calendar.addons.execute'
             ]

    creds = None
    
    #The file .token.pickle stores the user's access and refresh tokens, and is
    #created automatically when the authorization flow completes for the first
    #time.

    if os.path.isfile('{}/.token.pickle'.format(get_home_directory())):
        tp = '{}/.token.pickle'.format(get_home_directory())
        with open(tp, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.abspath('authentication/client_secret.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        tp = '{}/.token.pickle'.format(get_home_directory())
        with open(tp, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service
