from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

res = model.invoke("who is the president of the United States?")
print(res.content)
