from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vectors = embeddings.embed_documents(
    ["Hello world", "Goodbye world"]
)

print(len(vectors))
print(len(vectors[0]))