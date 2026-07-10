from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = ["Hello world", "Goodbye world"]

vectors = embeddings.embed_documents(texts)

print(len(vectors))
print(len(vectors[0]))