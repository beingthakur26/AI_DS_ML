# from langchain_community.document_loaders import PyPDFLoader
# # tokentext_splitter is a text splitter that splits text into chunks based on token count. It is useful for processing large documents and preparing them for natural language processing tasks.
# # it splits the text into chunks of a specified size, with an optional overlap between chunks. This can help preserve context and improve the quality of downstream tasks such as summarization, question answering, or information retrieval.
# from langchain_text_splitters import TokenTextSplitter

# data = PyPDFLoader("documents-loader/GRU.pdf")
# docs = data.load()

# splitter = TokenTextSplitter(
#     chunk_size=1000, 
#     chunk_overlap=10
# )
# chunks = splitter.split_documents(docs)

# print(len(chunks))
# print(chunks[0].page_content)

# # for i in chunks:    
# #     print(i.page_content)
# #     print("--------------------------------------------------")



from langchain_community.document_loaders import PyPDFLoader
# recurvise_character_text_splitter is a text splitter that splits text into chunks based on character count. It is useful for processing large documents and preparing them for natural language processing tasks.
# it splits the text into chunks of a specified size, with an optional overlap between chunks. This can help preserve context and improve the quality of downstream tasks such as summarization, question answering, or information retrieval.
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("documents-loader/GRU.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=10
)
chunks = splitter.split_documents(docs)

print(len(chunks))
print(chunks[0].page_content)

# for i in chunks:    
#     print(i.page_content)
#     print("--------------------------------------------------")