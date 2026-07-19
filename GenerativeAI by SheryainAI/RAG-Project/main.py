from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

# document loader: we can use the TextLoader to load the text document and then use the page content of the document as input to the model.
data = TextLoader("documents-loader/notes.txt")
docs = data.load()

# using mistral-small-2506 model: we can use the ChatMistralAI class to create a chat model using the mistral-small-2506 model. We can also set the temperature and streaming parameters for the model. The temperature parameter controls the randomness of the model's output, while the streaming parameter controls whether the model's output is streamed or returned as a single response.
# by this we can create a chat model that can be used to generate responses based on the input data. The model can be used to generate responses for various tasks such as question answering, text completion, and more.
chat = ChatMistralAI(model_name="mistral-small-2506", temperature=0.7, streaming=True)

# prompt template: we can use the page content of the document as input to the model and also decide roles for the prompt. Here we are using system and user roles. The system role is used to provide instructions to the model, while the user role is used to provide the input data.
template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{data}")]
)

# we can use the format_prompt method of the ChatPromptTemplate class to format the prompt with the input data. The formatted prompt can then be passed to the invoke method of the ChatMistralAI class to generate a response from the model.
prompt = template.format_prompt(data=docs[0].page_content)

# we can use the invoke method of the ChatMistralAI class to generate a response from the model. The response can then be printed to the console.
response = chat.invoke(prompt)

print(response.content)

