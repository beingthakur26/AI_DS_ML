from langchain_community.document_loaders import TextLoader

# text_splitter: text splitter to split the text into chunks
# chunks are used to create embeddings and store in vector database
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)

data = TextLoader("documents-loader/notes.txt")
docs = data.load()

chunks = splitter.split_documents(docs)

# print(docs)
# print(len(chunks))
for i in chunks:    
    print(i.page_content)
    print("--------------------------------------------------")