from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from . import prompt_template, ai_config

llm: ChatOpenAI = None
def connect() -> ChatOpenAI :
    return ai_config.connection_config()

def get_ai_design(user_input: str) -> str:
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_design   
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def get_ai_coding(user_input: str) -> str :
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_coding
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
