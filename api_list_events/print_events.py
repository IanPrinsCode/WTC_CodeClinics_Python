import time
from rich import print
from rich.text import Text
from rich.table import Table
from rich.padding import Padding

def print_user_events(events):
    """
    Uses a rich table to print out all the event items
    to standard output using colour.

    Parameters:
        events (dict): Personal calendar events.

    Returns:
        events (dict): Personal calendar events.
    """
    # Print for if no events were found for the specific call
    if len(events['items']) == 0:
        text = Text("No events.")
        text.stylize("bold dim italic rgb(75,130,194)")
        text = Padding(text, (2, 8), expand=False)
        print(text)
    else:
        for event in events['items']:
            
            # Formatting for personal calendar events
            if 'Code Clinic' not in event.get('summary', 'no summary'):

                # print title and id
                if 'summary' in event.keys():
                    table = Table(title=event['summary'],
                                header_style='rgb(75,130,194)',
                                style='rgb(77,77,77)')
                else:
                    table = Table(title='[NO TITLE]', title_style='red')    
                
                table.add_column("Attendees", justify="left")
                if 'start' in event.keys():
                    table.add_column(event['start']['dateTime'].split('T')[0],
                                justify="right",
                                header_style='white')
                elif 'originalStartTime' in event.keys():
                    ost = 'originalStartTime'
                    table.add_column(event[ost]['dateTime'].split('T')[0],
                                justify="right",
                                header_style='white')

                # Add date and times to table
                if 'start' in event.keys() and 'end' in event.keys():
                    table.add_row('','', style="white")
                    tm, st, ed, dt = 'Time: ', 'start', 'end', 'dateTime'
                    table.add_row(tm+event[st][dt].split('T')[1].split('+')[0]+
                                    ' => '+
                                    event[ed][dt].split('T')[1].split('+')[0],
                                    '', style="cyan")
                    table.add_row('','', style="white")
                else:
                    table.add_row('[TIME UNAVAILABLE]','', style="red")
                
                # Add attendees to table
                response = 'N/A'
                if 'attendees' in event.keys():
                    for item in event['attendees']:
                        if item['email'] != 'wethinkcode.codeclinic@gmail.com':
                            if item['responseStatus'] == 'accepted':
                                response = Text('Accepted')
                                response.stylize('white')
                            if item['responseStatus'] == 'needsAction':
                                response = Text('Needs Action')
                                response.stylize('rgb(75,130,194)')
                            if item['responseStatus'] == 'declined':
                                response = Text('Declined')
                                response.stylize('rgb(151,151,151)')
                            email = Text(item['email'])
                            email.stylize('rgb(75,130,194)')
                            table.add_row(email, response)
                else:
                    table.add_row('[NO ATTENDEES]', style="red")

                # Add padding and print individual table
                table = Padding(table, (2, 8), expand=False)
                print(table)

                # Time delay for displaying tables
                time.sleep(0.2)


            # Formatting for printing code clinic events
            else:

                # print title and id
                if 'summary' in event.keys():
                    table = Table(title=event['summary']+
                                    '\nID: '+
                                    event['description'],
                                    header_style='yellow',
                                    style='bold rgb(151,151,151)')
                else:
                    table = Table(title='[NO TITLE]', title_style='red')
                
                table.add_column("Attendees", justify="left")
                if 'start' in event.keys():
                    table.add_column(event['start']['dateTime'].split('T')[0],
                                        justify="right",
                                        header_style='white')
                elif 'originalStartTime' in event.keys():
                    ost = 'originalStartTime'
                    table.add_column(event[ost]['dateTime'].split('T')[0],
                                        justify="right",
                                        header_style='white')

                # Add date and times to table
                if 'start' in event.keys() and 'end' in event.keys():
                    table.add_row('','', style="white")
                    tm, st, ed, dt = 'Time: ', 'start', 'end', 'dateTime'
                    table.add_row(tm+event[st][dt].split('T')[1].split('+')[0]+
                                    ' => '+
                                    event[ed][dt].split('T')[1].split('+')[0],
                                    '', style="cyan")
                    table.add_row('','', style="white")
                else:
                    table.add_row('[TIME UNAVAILABLE]','', style="red")
                
                # Add attendees to table
                if 'attendees' in event.keys():
                    for item in event['attendees']:
                        if item['email'] != 'wethinkcode.codeclinic@gmail.com':
                            if item['comment'] == 'volunteer':
                                table.add_row(item['email'],'(Volunteer)',
                                                style="purple")
                            else:
                                table.add_row(item['email'],'(Bookee)',
                                                style="purple")
                else:
                    table.add_row('[NO ATTENDEES]', style="red")

                # Add padding and print individual table
                table = Padding(table, (2, 8), expand=False)
                print(table)

                # Time delay for displaying tables
                time.sleep(0.2)
