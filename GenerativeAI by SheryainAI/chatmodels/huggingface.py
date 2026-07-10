from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Why do parrots talk?")

print(response.content)