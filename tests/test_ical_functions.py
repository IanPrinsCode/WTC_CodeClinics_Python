from pathlib import Path
import unittest
import subprocess
import pickle
from io import StringIO
from unittest.mock import patch
import datetime
import os
import write_ical_files.create_ical_file as ci

class TestCalendar(unittest.TestCase):
    with open('./calendar_data/user_data.pickle', 'rb') as data:
        events = pickle.load(data)
    email = 'codeclinic@wethinkcode.co.za'
    
    def test_get_home_directory(self):
        from pathlib import Path
        home = str(Path.home())
        self.assertEqual(ci.get_home_directory(), home)

    def test_create_ical_file_output(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            ci.create_ical_file(TestCalendar.events, TestCalendar.email)
            self.assertEqual(fake_out.getvalue().strip(), 'Events written to iCal file.\nCheck the code_clinic_ical_files folder in your home directory')
    
    def test_if_ical_file_created(self):
        date = datetime.date.today()
        ci.create_ical_file(TestCalendar.events, TestCalendar.email)
        ical_string = f"{ci.get_home_directory()}/code_clinic_ical_files/{TestCalendar.email}: {date}.ics"
        self.assertTrue(os.path.exists(ical_string))
        if os.path.exists(ical_string):
            os.remove(ical_string)

    def test_time_format_conversion(self):
        self.assertEqual(ci.convert_time_format("2020-11-26T07:16:57.199Z"), "2020-11-26 07:16:57")    

if __name__ == '__main__':
    unittest.main()
