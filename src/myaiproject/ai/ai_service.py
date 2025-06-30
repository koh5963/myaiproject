import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from myaiproject.ai import prompt_template, ai_config

llm: ChatOpenAI = None
def connect() -> ChatOpenAI :
    return ai_config.connection_config()

def generate_design_docs(user_input: str) -> dict:
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_design   
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return json.loads(response.content)

def generate_code(user_input: str) -> dict :
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_coding_by
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    print(response.content)
    return json.loads(response.content)
