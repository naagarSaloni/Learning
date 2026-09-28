from .agent import agent


def run_agent(question: str) -> str:

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return result["messages"][-1].content