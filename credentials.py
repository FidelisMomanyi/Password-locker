import unittest

class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = []  # Empty credentials list
    # Init method up here

    
    def __init__(self, credentials_name,credentials_user_name,fname, lname,email, credentials_site, credentials_password):


        """
        __init__ method to  specify the attributes of a User object

        Args:
            user_name = user name
            email= email address
            fname = fname
            lname = lname
            credentials_site = the name of the credentials acccount
            credentials_password = the password of the account
        """
        self.credentials_name = credentials_name
        self.credentials_user_name = credentials_user_name
        self.fname = fname
        self.lname = lname
        self.email = email
        self.credentials_site = credentials_site
        self.credentials_password = credentials_password
        


    def save_credentials(self):
       '''
        save_credentials method save credentials objects into credentials_list
        '''

       Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls, credentials_name):
        """
        method that will return the credentials list

        """
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == credentials_name:
                Credentials.credentials_list.append(credentials)
                return Credentials.credentials_list

    @classmethod
    def find_by_email(cls, email):
        '''
        Method that takes in a email and returns the credentials that matches that email.

        Args:
            email: email to search for
        Returns :
            Credentials of person that matches the email.
        '''

        for credentials in cls.credentials_list:
            if credentials.email == email:
                return credentials
    
    @classmethod
    def find_credentials(cls, credentials_name):
        """
        method that takes in credentials name and returns the credentials that matches that name.

        Returns :
            credentials name that matches the input given.
        """

        for credentials in cls.credentials_list:
            if credentials_name == credentials_name:
                return credentials

    @classmethod
    def credentials_exist(cls, credentials_name):
        '''
        Method that checks if a credentials exists from the credentials list.

        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == credentials_name:
                return True
            

    


if __name__ == '__main__':
    unittest.main()
    
