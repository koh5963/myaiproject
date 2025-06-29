from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from myaiproject import prompt_template

def connect() -> ChatOpenAI :
    return ChatOpenAI(
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="not-needed",
        model_name="llama-3-8b-instruct-gradient-1048k"  # LM Studioでのモデル名に合わせて調整
    )

##
## 設計書作成
##
def get_ai_design(user_input: str):
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_design   
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    llm.invoke([HumanMessage(content=prompt)])

def get_ai_coding(user_input: str) -> str :
    ## input = "ユーザーが入力したパスのCSVファイルを読み込んで、TSVファイルに変換して入力CSVと同じフォルダに出力するツールを作成したい。出力するファイルパスのボリュームが実行ボリュームと異なる場合、ボリュームを移動してから出力すること。"
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template=prompt_template.template_coding
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
