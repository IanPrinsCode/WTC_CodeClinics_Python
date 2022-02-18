from os import system

def check_modules():
    """
    Checks if needed pip packages are installed. If not, it will install them.
    """
    installs = 'google-api-python-client '+ \
                'google-auth-httplib2 '+ \
                'google-auth-oauthlib '+ \
                'rich '+ \
                'ics'
    try:
        import googleapiclient.discovery
        import google_auth_oauthlib.flow
        import google.auth.transport.requests
        import rich
        import ics
    except ImportError:
        print("### Missing necessary installs ! ###")
        answer = input('Would you like to install needed packages? [y/N] ')
        if answer == 'y':
            print('### PERFORMING FIRST-TIME SETUP ###')
            print('Please be patient ..')
            system('pip3 install --upgrade {}'.format(installs))
            print('### TERMINATING PROGRAM TO APPLY INSTALLS ###')
            print('Please restart app.')
            quit()
        else:
            print('### TERMINATING PROGRAM: INSTALLS NEEDED! ###')
            quit()

check_modules()