from .model import model


def ask_ollama(question: str) -> str:

    response = model.invoke(question)

    return response.content