from .core import Graph, WeightedGraph
from . import algorithms
from paragon.graphs import (
    generate_normal_graph, 
    generate_normal_weighted_graph
)

from .algorithms import *
from .graphs import *


__version__ = "0.1.9"


__all__ = [
    "Graph",
    "WeightedGraph",
    "algorithms",
    "generate_normal_graph",
    "generate_normal_weighted_graph"
]