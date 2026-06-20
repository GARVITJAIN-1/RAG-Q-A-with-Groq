import os
import time
import streamlit as st

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# API Keys
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit Page Config
st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
)

st.title("📚 RAG Document Q&A With Groq")

# LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

# Prompt
prompt = ChatPromptTemplate.from_template(
    """
Answer the question based only on the provided context.

<context>
{context}
</context>

Question: {input}
"""
)


def create_vector_embeddings():

    if "vectors" in st.session_state:
        st.success("Vector Database already exists!")
        return

    try:
        start = time.time()

        st.write("Loading embedding model...")

        st.session_state.embeddings = OllamaEmbeddings(
            model="mxbai-embed-large"
        )

        st.write("Loading PDFs...")

        loader = PyPDFDirectoryLoader("./research_papers")

        docs = loader.load()

        st.write(f"PDF Pages Loaded: {len(docs)}")

        if len(docs) == 0:
            st.error("No PDFs found in research_papers folder.")
            return

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        final_documents = text_splitter.split_documents(docs)

        st.write(f"Chunks Created: {len(final_documents)}")

        if len(final_documents) == 0:
            st.error("No chunks generated.")
            return

        st.write("Creating FAISS Vector Store...")

        with st.spinner("Generating embeddings..."):
            vectors = FAISS.from_documents(
                final_documents,
                st.session_state.embeddings
            )

        st.session_state.vectors = vectors

        st.success(
            f"Vector DB Created Successfully! "
            f"({time.time()-start:.2f} sec)"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")


# Button
if st.button("Document Embedding"):
    create_vector_embeddings()

# User Query
user_prompt = st.text_input(
    "Ask a question from your research papers"
)

# Question Answering
if user_prompt:

    if "vectors" not in st.session_state:
        st.warning(
            "Please click 'Document Embedding' first."
        )
        st.stop()

    try:

        document_chain = create_stuff_documents_chain(
            llm,
            prompt
        )

        retriever = st.session_state.vectors.as_retriever(
            search_kwargs={"k": 3}
        )

        retrieval_chain = create_retrieval_chain(
            retriever,
            document_chain
        )

        start = time.time()

        response = retrieval_chain.invoke(
            {"input": user_prompt}
        )

        st.write("### Answer")
        st.write(response["answer"])

        st.write(
            f"Response Time: {time.time()-start:.2f} sec"
        )

        with st.expander(
            "Retrieved Document Chunks"
        ):
            for i, doc in enumerate(
                response["context"],
                start=1
            ):
                st.write("------------------------")
                st.write(doc.page_content)

    except Exception as e:
        st.error(f"Error: {str(e)}")