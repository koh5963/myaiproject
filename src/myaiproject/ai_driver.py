from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate

def connect() -> ChatOpenAI :
    return ChatOpenAI(
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="not-needed",
        model_name="llama-3-8b-instruct-gradient-1048k"  # LM Studioでのモデル名に合わせて調整
    )

def get_ai_response() -> str :
    input = "フルパスで入力されたCSVファイルを読み込んで、TSVファイルに変換して入力CSVと同じフォルダに出力するツールを作成したい。"
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template="""
        以下の要件に基づいて、Pythonで動作するシンプルなスクリプトを生成してください。
        要件: {user_requirement}

        出力はコードのみで、説明や補足は不要です。
        """
    )
    prompt = template.format(user_requirement=input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
