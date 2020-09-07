#!/usr/bin/env python3.6
from user import User
import getpass
import random
import string
dash = '-' * 60

def create_account(account_name,username,password,confirm_password):
    '''
    Function to create a new user
    '''
    new_user =  User(account_name,username,password,confirm_password)

    return new_user

def save_details(user):

    '''
    Function to save save_details
    '''
    user.save_detail()

def display_all_details():

     """
    function used to return all saved save_details
     """
     return User.display_all_details()

def check_existing_user(username):


    '''
    a function that check and return exissting accounts
    '''  
    return User.user_exist(username)


def generatePassword(num):
   genpass = '' 

   for n in rangea(num):
       x = random.randint(0,94)
       genpass += string.printable[x]

       return generatePassword