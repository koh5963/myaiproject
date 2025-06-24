"""Main module."""
from myaiproject import ai_driver, pyfile_creator

def create_code():
    response = ai_driver.get_ai_response()
    pyfile_creator.create_new(response)