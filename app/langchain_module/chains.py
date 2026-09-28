from .llm import llm
from .prompts import simple_prompt, chat_prompt
from .parsers import string_parser


# --------------------------------------------------
# Chain 1: Prompt → LLM
# --------------------------------------------------

simple_chain = simple_prompt | llm


# --------------------------------------------------
# Chain 2: Prompt → LLM → Parser
# --------------------------------------------------

simple_parsed_chain = (
    simple_prompt
    | llm
    | string_parser
)


# --------------------------------------------------
# Chain 3: Chat Prompt → LLM → Parser
# --------------------------------------------------

chat_chain = (
    chat_prompt
    | llm
    | string_parser
)


def explain_topic(topic: str):
    return simple_parsed_chain.invoke({
        "topic": topic
    })


def ask_question(question: str):
    return chat_chain.invoke({
        "question": question
    })