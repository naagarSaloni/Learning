from langchain_chroma import Chroma

from .embeddings import embeddings


def create_vectorstore(chunks):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="rag_documents"
    )

    return vectorstore