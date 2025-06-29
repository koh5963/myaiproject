from langchain_openai import ChatOpenAI

def connection_config() -> ChatOpenAI :
    return ChatOpenAI(
        openai_api_base="http://localhost:1234/v1",
        openai_api_key="not-needed",
        model_name="llama-3-8b-instruct-gradient-1048k"  # LM Studioでのモデル名に合わせて調整
    )