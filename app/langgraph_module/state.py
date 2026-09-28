from typing import TypedDict
#TypedDict  = define what keys our dictionary should contain.
#data that travels through the graph.Every node can read/update this state.

class GraphState(TypedDict):

    question: str

    category: str

    answer: str