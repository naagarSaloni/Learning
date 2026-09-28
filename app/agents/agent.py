from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from .tools import calculator, text_length


llm = ChatOpenAI(
    model="gpt-5.6-luna",
    temperature=0
)


tools = [
    calculator,
    text_length
]


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a helpful assistant.

First understand whether the user's question is:

1. programming
2. general

For programming questions:
- Answer as a programming teacher.
- Explain concepts in simple English.
- Do not use tools unless they are actually needed.

For general questions:
- Answer in simple English.
- Use the calculator tool when mathematical calculation is needed.
- Use the text_length tool when the user asks for the number of characters.

Choose the appropriate tool when necessary.

If no tool is needed, answer directly.
"""
)