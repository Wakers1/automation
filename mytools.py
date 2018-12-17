from getpass import getpass


def get_credentials():
    '''Prompts for and returns a username and password'''
    username = input('Enter Username: ')
    password = getpass('Enter Password: ')
    return username, password


