from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Example:
    25 * 4
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception:
        return "Could not calculate the expression."


@tool
def text_length(text: str) -> str:
    """
    Count the number of characters in a text.
    """

    return str(len(text))