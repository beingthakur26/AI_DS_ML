from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

data = TextLoader("documents-loader/notes.txt")
docs = data.load()

chat = ChatMistralAI(model_name="mistral-small-2506", temperature=0.7, streaming=True)

template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{data}")]
)

prompt = template.format_prompt(data=docs[0].page_content)
response = chat.invoke(prompt)

print(response.content)

