from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from .loader import load_documents
from .splitter import split_documents
from .vectorstore import create_vectorstore
from .retriever import create_retriever


llm = ChatOpenAI(
    model="gpt-5.6-luna",
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the question using only the provided context.

If the answer is not present in the context,
say that you do not know based on the provided documents.

Context:
{context}

Question:
{question}

Answer:
"""
)


def create_rag():

    # 1. Load documents
    documents = load_documents(
        "data/documents/sample.txt"
    )

    # 2. Split documents
    chunks = split_documents(documents)

    # 3. Create vector store
    vectorstore = create_vectorstore(chunks)

    # 4. Create retriever
    retriever = create_retriever(vectorstore)

    return retriever


def ask_rag(question: str):

    retriever = create_rag()

    # Retrieve relevant documents
    documents = retriever.invoke(question)

    # Combine retrieved chunks
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Create prompt
    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    # Ask LLM
    response = llm.invoke(messages)

    return response.content