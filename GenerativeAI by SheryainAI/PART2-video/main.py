from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

chat = ChatMistralAI(model_name="mistral-small-2506", temperature=0.7, streaming=True)

response = chat.invoke("What is the capital of France?")

print(response.content)

