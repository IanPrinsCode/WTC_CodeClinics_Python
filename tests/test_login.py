import unittest
from io import StringIO
import os
from login.login import verify_user_credentials, check_token_exists, token_time_valid, update_token, get_home_directory
from tests.helper_functions import capture_input_output



class TestLogin(unittest.TestCase):

    def test_verify_user_credentials_returns_true(self):
        with capture_input_output(StringIO('dranger@student.wethinkcode.co.za\n')) as (out, err):
            self.assertTrue(verify_user_credentials('dranger@student.wethinkcode.co.za'))

    def test_verify_user_credentials_returns_false(self):
        with capture_input_output(StringIO('dranger@minkwhales.co.za\n')) as (out, err):
            self.assertFalse(verify_user_credentials('dranger@student.wethinkcode.co.za'))

    def test_check_token_exists_returns_true(self):
        if os.path.isfile('{}/.token.pickle'.format(get_home_directory())):
            self.assertTrue(check_token_exists())        


if __name__ == "__main__":
    unittest.main()