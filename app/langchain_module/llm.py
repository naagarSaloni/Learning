from langchain_openai import ChatOpenAI, OpenAIEmbeddings


# Main LLM
llm = ChatOpenAI(
    model="gpt-5.6-luna",
    temperature=0
)


# Embedding model for RAG
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)