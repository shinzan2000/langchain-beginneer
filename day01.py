from langchain_openai import ChatOpenAI

# OpenAIのモデルを指定
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 質問を明確にする
prompt = "LangChainとは何か、AIアプリケーション開発における役割と主な機能について簡潔に説明してください。"

# AIからの応答を取得
response = llm.invoke(prompt)

print(response.content)
