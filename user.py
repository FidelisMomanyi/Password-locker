import unittest
from credentials import Credentials  # import the credentials class


class User:
    """
    class that generates new instances of users
    """

    user_list=[] # Empty user list

    def __init__(self,user_name,user_password):
       """
        define objects (user_name, user_password)
        """

       self.user_name = user_name
       self.user_password = user_password

    def save_user_details(self):
        """
        save_contact method saves user objects into user_list
        """
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class list
        """
        return cls.user_list

    @classmethod
    def check_existing_users(cls, user_name,user_password):
        """
        method that checks if a user exists in the user list
        Args:
            name: name of the user to search 

        Returns:
            Boolean: true/false depending on whether  user exists
        """

        for user in cls.user_list:
            if user.user_name == user_name and user.user_password==user_password:
                return True
            else:
                return False


    @classmethod
    def log_in(cls, user_name, user_password):
        """
        method for user to log-in to their accounts

        Args:
            user_name : name of user
            user_password : password of the user

        Returns:
            credentials list 

        """

       # search for the user  in user list
       
        for User in cls.user_list:

            if User.user_name == user_name and User.user_password == user_password:

                return Credentials.credentials_list


        return False


if __name__ == '__main__':
        unittest.main()
