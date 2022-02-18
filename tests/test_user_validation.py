import unittest
import user_validation.command_validation as cv


class MyTestCase(unittest.TestCase):
    def test_check_for_normal_command_true(self):
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_calendar']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','booked_slots']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_volunteer_slots']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','open_slots']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_calendar','6']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_calendar','365']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','book_slot','c2hg3yy3u498f9dfu3n290d']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','cancel_booking','c2hg3yy3u498f9dfu3n290d']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','delete_slot','c2hg3yy3u498f9dfu3n290d']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','volunteer_slot','2021-01-08','12:00']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_calendar', '2','iCal']))
        self.assertTrue(cv.check_for_normal_command(['run_cli.py','my_calendar', 'iCal']))


    def test_check_for_normal_command_false(self):
        self.assertFalse(cv.check_for_normal_command(['run_cli.py']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','login']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','pineapple']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','pineapple','Pacific Ocean']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','pineapple','Pacific Ocean','Permangenate']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','my_calendar','display']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','my_calendar','1a1']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','booked_slots','6']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','my_volunteer_slots','6']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','open_slots','6']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','booked_slots','please']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','book_slot']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','cancel_booking']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','delete_slot']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','volunteer_slot']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','volunteer_slot','2021-01-08']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','delete_slot','c2hg3yy3u498f9dfu3n290d','help']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','nothing','help']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','help','open_slots']))
        self.assertFalse(cv.check_for_normal_command(['run_cli.py','my_calendar', 'iCal', '2']))

    def test_check_for_normal_help_true(self):
        commands = ['my_calendar','booked_slots','my_volunteer_slots','open_slots','book_slot','cancel_booking','delete_slot','volunteer_slot']
        for x in commands:
            self.assertTrue(cv.check_for_help_command(['run_cli.py',x,'help']))

    def test_check_for_normal_help_false(self):
        self.assertFalse(cv.check_for_help_command(['run_cli.py','help','help']))
        self.assertFalse(cv.check_for_help_command(['run_cli.py','okay','help']))
        self.assertFalse(cv.check_for_help_command(['run_cli.py','help','book_slot']))
        self.assertFalse(cv.check_for_help_command(['run_cli.py','help']))

    def test_date_validation(self):
        self.assertTrue(cv.date_validation('2021-01-01'))
        self.assertFalse(cv.date_validation('2021-01-33'))
        self.assertFalse(cv.date_validation('2021-32-01'))
        self.assertFalse(cv.date_validation('100000-01-01'))
        self.assertFalse(cv.date_validation('2021-01'))
        self.assertFalse(cv.date_validation('2021-01-01-01'))
        self.assertFalse(cv.date_validation('200A-01-01'))

    def test_time_validation(self):
        self.assertTrue(cv.time_validation('12:33')) 
        self.assertTrue(cv.time_validation('01:05')) 
        self.assertTrue(cv.time_validation('1:33')) 
        self.assertTrue(cv.time_validation('12:2')) 
        self.assertFalse(cv.time_validation('43:02')) 
        self.assertFalse(cv.time_validation('09:99')) 
        self.assertFalse(cv.time_validation('77:72')) 
        self.assertFalse(cv.time_validation('4B:02')) 


if __name__ == '__main__':
    unittest.main
