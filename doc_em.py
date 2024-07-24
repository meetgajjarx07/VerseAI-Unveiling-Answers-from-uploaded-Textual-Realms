import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader, TextLoader, CSVLoader




def select_loader(file_path):
    _, ext = os.path.splitext(file_path)
    if ext in ['.txt', '.md']:
        return TextLoader(file_path, encoding='utf-8')
    elif ext in ['.pdf', '.pptx', '.docx', '.doc', '.xlsx']:
        return UnstructuredFileLoader(file_path, encoding='utf-8')
    else:
        raise ValueError(f"No loader available for the file type: {ext}")

def knowledge_load(path,hf_embeddings):
    directory_path = path

    loader = DirectoryLoader(
        path=directory_path,
        loader_cls=select_loader,
        recursive=True,
        show_progress=True
    )

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding=hf_embeddings)

    return 1,vectorstore

# knowledge_load('tmp',HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5"))