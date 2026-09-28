#Edges decide where the graph goes next.
from .state import GraphState


def decide_next_node(state: GraphState):

    category = state["category"]

    if category == "programming":
        return "programming"

    return "general"