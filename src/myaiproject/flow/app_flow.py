"""Main module."""
from myaiproject.output import output_writer
from myaiproject.ai import ai_service

def create_code():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_service.get_ai_coding(user_requirements)
    output_writer.create_new(response)

def create_design():
    user_requirements = input("Please enter your requirements... : ")
    if len(user_requirements) == 0:
        return

    response = ai_service.get_ai_design(user_requirements)
    print(response)
