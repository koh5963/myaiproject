"""Main module."""
from myaiproject import ai_driver, pyfile_creator

def create_code():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_driver.get_ai_response(user_requirements)
    pyfile_creator.create_new(response)