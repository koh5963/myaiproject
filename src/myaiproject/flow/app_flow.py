"""Main module."""
from myaiproject.output import output_writer
from myaiproject.ai import ai_service
from myaiproject.constants import const

def create_code():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_service.generate_code(user_requirements)
    print(response[const.JSON_KEY_EXPLANATION])
    output_writer.write_file(response[const.JSON_KEY_OUTPUT])

def create_design():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_service.generate_design_docs(user_requirements)
    print(response)
