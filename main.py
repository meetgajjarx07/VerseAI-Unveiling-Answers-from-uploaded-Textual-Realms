import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module='huggingface_hub')


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.vectorstores import Chroma
from typing import List
import streamlit as sl
from doc_em import knowledge_load
import os



def load_embedding_model():
    hf_embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")
    return hf_embeddings


def load_prompt():
        prompt = """You are best customer support chatbot agent. you will help customer from context given and answer it in very respectful manner. so answer like that in simple and step by step point wise manner. Do not write answer in Mail format.
        \n\n# Context:\n{context}\n\n
        #Question:\n{question}
        if the answer is not in the pdf , answer "Please Ask Qustion from Given Files"
        """
        prompt = ChatPromptTemplate.from_template(prompt)
        return prompt


def load_llm():
        llm = ChatGroq(groq_api_key='ADD YOUR GROQ API KEY', model_name='llama3-70b-8192')
        return llm


def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

flg = 0
knowledgeBase = None
if __name__=='__main__':
        sl.header("VerseAI: Unveiling Answers from Uploaded Textual Realms")
        hf_embeddings = load_embedding_model()
        llm=load_llm()
        prompt=load_prompt()
        
        uploaded_files = sl.file_uploader("Select the text that beckons your inquiry", accept_multiple_files=True)
        query=sl.text_input('Scribe your question here, and let answers weave their tale.')
        
        
        
        if query:
            if uploaded_files:

                print(f'\n{flg}\n')

                if flg == 0:
                    for uploaded_file in uploaded_files:

                        bytes_data = uploaded_file.read()
                        os.system('mkdir "tmp"')
                        file_path = os.path.join('tmp', uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(bytes_data)                    

                    flg, knowledgeBase = knowledge_load('tmp', hf_embeddings)

                    os.system('rmdir /S /Q tmp')


                similar_embeddings=knowledgeBase.similarity_search(query)
                print('\n---------------------------\n')
                print(similar_embeddings[0].page_content)
                similar_embeddings=Chroma.from_documents(similar_embeddings, hf_embeddings)
                print('\n---------------------------\n')

                
                retriever = similar_embeddings.as_retriever()

                rag_chain = (
                        {"context": retriever | format_docs, "question": RunnablePassthrough()}
                        | prompt
                        | llm
                        | StrOutputParser()
                    )
                response=rag_chain.invoke(query)
                sl.write(response)
