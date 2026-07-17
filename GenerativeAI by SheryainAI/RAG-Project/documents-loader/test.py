from langchain_community.document_loaders import TextLoader

data = TextLoader("documents-loader/notes.txt")
docs = data.load()

print(docs)