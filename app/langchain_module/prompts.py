from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate
)


# Simple prompt
simple_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
Explain {topic} in simple English.

Give:
1. Definition
2. Simple explanation
3. One example
"""
)


# Chat prompt
chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful programming teacher. "
        "Explain technical concepts in simple English."
    ),
    (
        "human",
        "{question}"
    )
])


# RAG prompt
rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a helpful assistant.

Answer the user's question using ONLY the
provided context.

If the answer is not available in the context,
say: "I don't know based on the provided document."

Context:
{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])