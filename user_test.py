import unittest # Import the unittest module
from user import User # Import the User class
from credentials import Credentials # Import the Credentials class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("FidelisMomanyi","FidePozee") # create user object
    

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []

    def test_init(self):
        """
        test_init test case to test if object utilizes proper instantiation
        """
        self.assertEqual(self.new_user.user_name,"FidelisMomanyi")
        self.assertEqual(self.new_user.user_password,"FidePozee")

    def test_save_user(self):
        """
         test case to test if the user object is saved in
         users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        """
            this test-case method gives users the ability to save multiple account details
        """
        self.new_user.save_user_details()
        test_user = User("Fidelis","fidel09")  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.user_list), 2)

    
    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.user_list)
   
    def test_log_in(self):
        """
        test to establish whether user can log-in to their credentials
        """
        # start by saving user
        self.new_user.save_user_details()

        test_user = User("Fidelis","fidel09")

        test_user.save_user_details()

        found_credentials = User.log_in("Fidelis","fidel09")

        self.assertEqual(found_credentials,Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()

    
