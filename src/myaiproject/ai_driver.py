from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate

def connect() -> ChatOpenAI :
    return ChatOpenAI(
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="not-needed",
        model_name="llama-3-8b-instruct-gradient-1048k"  # LM Studioでのモデル名に合わせて調整
    )

def get_ai_response(user_input: str) -> str :
    ## input = "ユーザーが入力したパスのCSVファイルを読み込んで、TSVファイルに変換して入力CSVと同じフォルダに出力するツールを作成したい。出力するファイルパスのボリュームが実行ボリュームと異なる場合、ボリュームを移動してから出力すること。"
    template = PromptTemplate(
        input_variables=["user_requirement"],
        template="""
        あなたはコーディングのプロフェッショナルです。
        以下の要件に基づいて、Pythonで動作するシンプルなスクリプトを生成してください。
        出力はコードのみで、説明や補足は絶対に出力しないでください。

        要件: {user_requirement}
        """
    )
    prompt = template.format(user_requirement=user_input)

    llm = connect()
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
