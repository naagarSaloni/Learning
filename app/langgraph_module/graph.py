from langgraph.graph import (
    StateGraph,
    START,
    END
)

from .state import GraphState

from .nodes import (
    classify_question,
    programming_answer,
    general_answer
)

from .edges import decide_next_node


# ============================================
# CREATE GRAPH
# ============================================

builder = StateGraph(GraphState)


# ============================================
# ADD NODES
# ============================================

builder.add_node(
    "classify",
    classify_question
)

builder.add_node(
    "programming",
    programming_answer
)

builder.add_node(
    "general",
    general_answer
)


# ============================================
# ADD NORMAL EDGE
# ============================================

builder.add_edge(
    START,
    "classify"
)


# ============================================
# ADD CONDITIONAL EDGE
# ============================================

builder.add_conditional_edges(
    "classify",
    decide_next_node,
    {
        "programming": "programming",
        "general": "general"
    }
)


# ============================================
# END EDGES
# ============================================

builder.add_edge(
    "programming",
    END
)

builder.add_edge(
    "general",
    END
)


# ============================================
# COMPILE
# ============================================

graph = builder.compile()