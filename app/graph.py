import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END


load_dotenv()


class ChatState(TypedDict):
    message: str
    answer: str


llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0.2
)


def generate_answer(state: ChatState):
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question clearly and simply.

User question:
{state["message"]}
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return {
        "answer": response.content
    }


workflow = StateGraph(ChatState)

workflow.add_node(
    "generate_answer",
    generate_answer
)

workflow.add_edge(
    START,
    "generate_answer"
)

workflow.add_edge(
    "generate_answer",
    END
)

graph = workflow.compile()