#!/usr/bin/env python3.8

from credentials import Credentials
from user import User
import random

"""
Run module
"""


def create_user(user_name, user_password):
    '''
    Function that creates new user
    '''
    new_user = User(user_name, user_password)
    return new_user


def save_user_details(User):
    '''
    saves user details
    '''
    User.save_user_details()

def find_user(user_name):
    """
    function to find credentials based on credentials_name 
    """
    return User.find_user(user_name)

def check_existing_users(user_name, user_password, user_log_in_name, user_log_in_password):
    '''
    Function that checks if a user account  exists
    '''
    user_log_in_name = User(user_name)
    user_log_in_password = User(user_password)
    if user_log_in_name != False and user_log_in_password != False:
        return User.User_exists


def display_user():
    '''
    display users
    '''
    return User.display_users()


def user_log_in(user_name, user_password):
    '''
    Function to allow user to log-in to their credentials account
    '''
    user_log_in = User.log_in(user_name, user_password)
    if user_log_in != False:
        return User.log_in(user_name, user_password)


def create_credentails(credentials_name, credentials_user_name, fname, lname, email, credentials_password, credentials_site):
    '''
    Function to create new credentials
    '''

    new_credentails = Credentials(credentials_name, credentials_user_name,
                                  fname, lname, email, credentials_password, credentials_site)

    return new_credentails


def save_credentials(credentials_name):
    '''
    Function to save credentials
    '''
    credentials_name.save_credentials()


def check_existing_credentials(credentials_name):
    '''
    Function that checks if a user credentials_name exists
    '''
    return Credentials.credentials_exist(credentials_name)


def display_credentials(credentials_name):
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials(credentials_name)


def find_credentials(credentials_name):
    """
    function to find credentials based on credentials_name 
    """
    return Credentials.find_credentials(credentials_name)


def delete_credentials(credentials_name):
    '''
    Function to delete credentials
    '''
    credentials_name.delete_credentials()


def main():
    print("Hello Welcome to PASSWORDLOCKER")

    while True:

        print("""Short codes:
        nw - Create a new passwordlocker account \n
        lg - Log-in to your already existing account on passwordlocker \n
         """)
        short_code = input().lower()

        if short_code == "nw":
            """
            short_code to create new account on passwordlocker
            """
            print("\n")
            print(" New passwordlocker account")
            print("-*-"*10)

            print("User name ...")
            user_name = input()

            print("password ...")
            user_password = input()
            save_user_details(create_user(user_name, user_password))

            if save_user_details(create_user(user_name, user_password)) == save_user_details(create_user(user_name, user_password)):
                print("\n")
                print(
                    f"Welcome {user_name} Your account has been created successfully!\n")
                continue
            else:
                (user_name, user_password) == None
                print("\n")
                print("Invalid user name or password, try again")
                print("\n")
                break
        elif short_code == "lg":
            """
            short_code to allow user to Log-in to already existing account on passwordlocker 
            """
            print("\n")
            print("*"*10)
            print("Log-in to your Passwordlocker Account")
            print("Enter the user name")
            user_log_in_name = input()

            print("Enter the password")
            user_log_in_password = input()

            user_log_in(user_log_in_name, user_log_in_password)
            if check_existing_users != False:
                print("\n")
                print("Welcome.")
                print("\n")
                print("You have successfully logged into your Account")
                print("\n")
                print("*Use the following codes to navigate*")
                print("\n")

            else:
                user_log_in(user_name, user_password) == None
                print("\n")
                print("Invalid user name or password, try again or Create a New Account")
                print("\n")
                break
        else:
            print("invalid input")
            break
        while True:

            print("""Use these short codes:
            cc - create a new credentials_user account with a user_defined password,\n
            can -create a new_credentials_user account with auto-generated password,\n
            sv - add credentials to an already exiting account,\n
            dc - display credentials\n
            del - delete an existing credentials account\n
            ex - Exit """)
            short_code = input().lower()

            if short_code == "cc":
                print("new credentials_user_name with a user_defined password")
                print("-*-" * 10)

                print("credentials name ...")
                credentials_name = input()

                print("First name ....")
                fname = input()

                print("Last name ...")
                lname = input()

                print("Enter username ...")
                credentials_user_name = input()

                print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                credentials_site = input()

                print("Email Address ...")
                email = input()

                print("Enter a password")
                credentials_password = input()

                save_credentials(create_credentails(credentials_name, credentials_user_name,
                                 fname, lname, email, credentials_password, credentials_site))
                print("\n")
                print(
                    f"A new {credentials_name } account by { fname } has successfully been created")
                print(
                    f"The username is {credentials_user_name} and the password is {credentials_password} ")
                print("\n")

            elif short_code == "can":
                print("new credentials_user_name with auto-generated password")
                print("-*-"*10)

                print("credentials name ...")
                credentials_name = input()

                print("First name ....")
                fname = input()

                print("Last name ...")
                lname = input()

                print("Enter username ...program will generate a password for you")
                credentials_user_name = input()

                print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                credentials_site = input()

                print("Email Address ...")
                email = input()

                password_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                credentials_password = "".join(
                    random.sample(password_generator, 8))
                print("Password")

                save_credentials(create_credentails(credentials_name, credentials_user_name,
                                 fname, lname, email, credentials_password, credentials_site))
                print("\n")
                print(
                    f"The username is {credentials_user_name} and the password is {credentials_password} ")
                print("\n")

            elif short_code == "sv":
                print("\n")
                print("add credentials to an already exiting account")
                print("-*-"*10)

                print("credentials name ...")
                credentials_name = input()

                print("user name ...")
                credentials_user_name = input()

                print("Email Address ...")
                email = input()

                print("Password...")
                credentials_password = input()

                print("""What account would like to create credentials for?\n
                               eg; Facebook""")
                credentials_site = input()

                save_credentials(create_credentails(credentials_name, fname, lname,
                                 credentials_user_name, email, credentials_password, credentials_site))

                print("\n")
                print(
                    f"Credentials for {credentials_name} have been successfully saved !\n")
                print("\n")

            elif short_code == "dc":
                print("\n")
                print("display credentials")
                print("-*-"*10)
                print("display credentials for ...")
                credentials_name = input()

                if  find_credentials(credentials_name):
                    display_credentials(credentials_name)
                    print("\n")
                    print(f"{credentials_name}\'s credentials")
                    print("*"*10)
                    print(f"Site ..... {credentials_site}")
                    print(f"UserName .... {credentials_user_name}")
                    print(f"Email .... {email}")
                    print(f"Password .... {credentials_password}")
                    print("*"*10)
                else:
                    print("\n")
                    print("Sorry, there is no account maching your details.")
                    print("\n")

            elif short_code == "del":

                print("Enter name of credentials you want to delete")
                credentials_name = input()

                if find_credentials(credentials_name):
                    delete_credentials(credentials_name)
                    print(f"Your stored credentials for: {credentials_name} has been deleted Successfully \n")
                else:
                    print(" The Credentials does not Exist ")

            elif short_code == "ex":
                print("Bye ....")

            else:
                print("Invalid command")
                break


if __name__ == '__main__':
    main()
