from dotenv import load_dotenv


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# LANGCHAIN
# ============================================================

from app.langchain_module.chains import (
    explain_topic,
    ask_question
)


# ============================================================
# LANGGRAPH
# ============================================================

from app.langgraph_module.graph import graph


# ============================================================
# AGENT
# ============================================================

from app.agents.executor import run_agent


# ============================================================
# RAG
# ============================================================

from app.rag.rag_chain import ask_rag


# ============================================================
# OLLAMA
# ============================================================

from app.ollama.client import ask_ollama


# ============================================================
# OBSERVABILITY
# ============================================================

from app.observability.tracing import trace


# ============================================================
# MAIN
# ============================================================

def main():

    # ========================================================
    # 1. LANGCHAIN - LLM CALL
    # ========================================================

    print("\n" + "=" * 60)
    print("1. LANGCHAIN - LLM CALL")
    print("=" * 60)

    answer = ask_question(
        "What is LangChain?"
    )

    print("\nAnswer:")
    print(answer)


    # ========================================================
    # 2. LANGCHAIN - PROMPT + CHAIN
    # ========================================================

    print("\n" + "=" * 60)
    print("2. LANGCHAIN - PROMPT + CHAIN")
    print("=" * 60)

    answer = explain_topic(
        "FastAPI"
    )

    print("\nAnswer:")
    print(answer)


    # ========================================================
    # 3. LANGGRAPH
    # ========================================================

    print("\n" + "=" * 60)
    print("3. LANGGRAPH")
    print("=" * 60)

    question = input(
        "\nAsk a LangGraph question: "
    )

    result = graph.invoke({
        "question": question,
        "category": "",
        "answer": ""
    })

    print("\nCategory:")
    print(result["category"])

    print("\nLangGraph Answer:")
    print(result["answer"])


    # ========================================================
    # 4. AGENT
    # ========================================================

    print("\n" + "=" * 60)
    print("4. AGENT")
    print("=" * 60)

    question = input(
        "\nAsk the Agent something: "
    )

    answer = run_agent(question)

    print("\nAgent Answer:")
    print(answer)


    # ========================================================
    # 5. RAG
    # ========================================================

    print("\n" + "=" * 60)
    print("5. RAG")
    print("=" * 60)

    question = input(
        "\nAsk something about the documents: "
    )

    answer = ask_rag(question)

    print("\nRAG Answer:")
    print(answer)


    # ========================================================
    # 6. OLLAMA
    # ========================================================

    print("\n" + "=" * 60)
    print("6. OLLAMA - LOCAL MODEL")
    print("=" * 60)

    question = input(
        "\nAsk Ollama something: "
    )

    answer = ask_ollama(question)

    print("\nOllama Answer:")
    print(answer)


    # ========================================================
    # 7. OBSERVABILITY
    # ========================================================

    print("\n" + "=" * 60)
    print("7. OBSERVABILITY")
    print("=" * 60)

    @trace("Simple LLM Operation")
    def traced_question(question):

        return ask_question(question)

    question = input(
        "\nAsk something to test tracing: "
    )

    answer = traced_question(question)

    print("\nTraced Answer:")
    print(answer)


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    main()