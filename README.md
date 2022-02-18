# Code_Clinics Overview:

This program is a group project at WeThinkCode_. We were tasked with creating a CLI booking
system for use by the student body. The Code Clinics are 30 minute long sessions where one
student helps another understand a part of the curriculum they are having trouble with.

The booking system uses the Google Calendar API to create events. Students can use the
CLI for a variety of functions, and all events and bookings rely on the google calendar
api and will sync with the student's Google Calendar. The Code Clinics booking system 
takes command line arguments as input. Currently there are 9 different commands.

Students can volunteer 30 minute long slots. They can specify a date and time, as well 
as a topic. If they wish to delete a slot they have created, they are able to do so 
providing that another student has not booked that slot.

Students can view the slots that others have opened and make bookings for those slots. 
A booking can be cancelled at any time.

There are a variety of ways in which the events can be displayed via the terminal:

1. Students can view their personal calendar events.
2. Students can view the slots they have booked.
3. Students can view the slots they have volunteered.
4. Students can view slots that are available for booking.

We have included a comprehensive 'help' feature which will display all the possible 
commands, as well as specific help information for each command.

# TO RUN:

Navigate to the project directory via your terminal. Running commands for the first
time on your system, you will be prompted to install the required 3rd party dependencies.
You will also be prompted to perform google OAuth so that the Code Clinics has access
to your google calendar. Once you have installed the necessary dependencies and you have
authenticated yourself, you are ready to use the code clinics CLI.

Run 'python3 code_clinics.py' followed by one of the 9 possible commands and its required 
arguments. Here is a list of the commands and what they do:

**To view your personal calendar, run:**

    python3 code_clinics.py my_calendar *number* iCal

This will display the events on your personal calendar. The **number** and **iCal** arguments
are both optional. If you enter a number as an argument, the CLI will display events for
that number of days. Without this argument, the number of days will default to 7. If you 
add 'iCal' as an argument the events will be written to an iCal file which is saved in 
your home directory inside a folder named 'code_clinic_ical_files.

**To view the slots you have booked, run:**

    python3 code_clinics.py booked_slots

This will display the slots you have booked.

**To view the slots you have volunteered, run:**

    python3 code_clinics.py my_volunteer_slots

This will display all the slots you have volunteered.

**To view slots other people have volunteered, run:**

    python3 code_clinics.py open_slots

This will display all the slots that are available for booking.

**To book a slot, run:**

    python3 code_clinics.py book_slot *id*

This will book the slot. The **id** argument is mandatory. If you
display open slots, you will see the 3-digit event ID displayed
beneath the title of the code clinic. Once you find a code clinic
slot with a time and a topic that works for you, you can copy or
memorise that ID and use it to book a slot.

**To cancel a booking, run:**

    python3 code_clinics.py cancel_booking *id*

This will remove you as the event attendee from an event that
you have bookied. The **id** argument is mandatory. If you
display your booked slots, you will see the 3-digit event ID displayed
beneath the title of the code clinic. Once you find the code clinic
slot you wish to cancel, you can copy or memorise the ID and use it 
to cancel your booking.

**To volunteer a slot, run:**

    python3 code_clinics.py volunteer_slot *date* *time*

This will open a volunteer slot. You will be prompted to enter a
topic. Both **date** and **time** are mandatory arguments. Date must
be in the format yyyy-mm-dd and time must be in the format hh:mm, i.e.

    python3 code_clincs.py volunteer_slot 2020-01-30 17:00.

**To delete a slot you volunteered, run:**

    python3 code_clinics.py delete_slot *id*

This will delete a slot you have volunteered. Note that it is not
possible to delete a slot if someone has already booked it. The 
**id** argument is mandatory. If you display your volunteer slots, 
you will see the 3-digit event ID displayed beneath the title of 
the code clinic. Once you find the code clinic slot you wish to 
delete, you can copy or memorise the ID and use it to delete your 
slot.

**To display help information, run:**

    python3 code_clinics.py help

This will display a the help information for the Code Clinics
CLI. Using any invalid commands will also bring up the help 
menu.

Additionally, if you add help, --help or -h as an argument in
combination with any of the commands above, you will receive
help information relating to that command.

    python3 code_clinics.py book_slot help
    python3 code_clinics.py book_slot -h
    python3 code_clinics.py book_slot --help

Running any of the lines above will bring up help information
for the 'book_slot' command.

**PLEASE NOTE** This software was developed for the Debian operating system. We can
not guarantee that it will work on other operating systems.

# Running Unit Tests:

If you wish to run the unittests we created for the project, make
sure you are in the main directory of the program, then run:

    python3 test_main.py

This will run all the unit tests contained in the tests package.


# To uninstall the packages needed by our program, run the following command:

    pip3 uninstall google-api-python-client google-auth-httplib2 google-auth-oauthlib rich ics

# Reporting Issues:

If you have issues with the CLI, please contact one of the students
who worked on the project. Here are the usernames for the developers:

dranger, iprins, jmather, aebrahim, mumuller, asiguqa, wkoela.

    
