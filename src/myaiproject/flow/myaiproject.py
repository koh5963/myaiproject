"""Main module."""
from myaiproject.output import pyfile_creator
from myaiproject.ai import ai_driver

def create_code():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_driver.get_ai_coding(user_requirements)
    pyfile_creator.create_new(response)

def create_design():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_driver.get_ai_design(user_requirements)
    print(response)
