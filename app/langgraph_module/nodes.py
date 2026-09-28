#actual work/functions performed by the graph
from langchain_openai import ChatOpenAI

from .state import GraphState


llm = ChatOpenAI(
    model="gpt-5.6-luna",
    temperature=0
)


# ============================================
# NODE 1: CLASSIFY
# ============================================

def classify_question(state: GraphState):

    question = state["question"]

    prompt = f"""
Classify this question into exactly one category.

Categories:
- programming
- general

Question:
{question}

Return only the category name.
"""

    response = llm.invoke(prompt)

    category = response.content.strip().lower()

    if "programming" in category:
        category = "programming"
    else:
        category = "general"

    return {
        "category": category
    }


# ============================================
# NODE 2: PROGRAMMING ANSWER
# ============================================

def programming_answer(state: GraphState):

    question = state["question"]

    prompt = f"""
You are a programming teacher.

Answer this question in simple English:

{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ============================================
# NODE 3: GENERAL ANSWER
# ============================================

def general_answer(state: GraphState):

    question = state["question"]

    prompt = f"""
Answer this question in simple English:

{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }