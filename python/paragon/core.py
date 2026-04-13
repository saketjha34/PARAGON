from __future__ import annotations
from typing import List, Tuple, Iterable, Optional, Union

from ._paragon import Graph as _Graph
from ._paragon import WeightedGraph as _WeightedGraph


# ================= GRAPH ================= #
class Graph(_Graph):
    """
    Unweighted graph data structure.

    This class provides a Python interface over a high-performance C++
    graph implementation. It supports flexible initialization and
    efficient graph operations.

    Initialization styles
    ---------------------
    1. Graph(vertices)
    2. Graph(adjacency_list)
    3. Graph(vertices, edges)

    Notes
    -----
    - Nodes are indexed from 0 to V-1
    - Uses adjacency list internally
    - Supports both directed and undirected graphs
    """

    def __init__(
        self,
        vertices: Union[int, List[List[int]]],
        edges: Optional[Iterable[Tuple[int, int]]] = None,
        directed: bool = False,
    ) -> None:
        """
        Initialize a graph.

        Parameters
        ----------
        vertices : int or List[List[int]]
            - If int → number of vertices
            - If List → adjacency list

        edges : Iterable[Tuple[int, int]], optional
            List of edges (u, v)

        directed : bool, default=False
            Whether the graph is directed

        Raises
        ------
        TypeError
            If invalid arguments are provided

        Examples
        --------
        >>> g = Graph(5)
        >>> g = Graph([[1, 2], [0], [0]])
        >>> g = Graph(3, [(0, 1), (1, 2)])
        """

        if isinstance(vertices, list):
            super().__init__(vertices, directed)

        elif isinstance(vertices, int) and edges is not None:
            super().__init__(vertices, list(edges), directed)

        elif isinstance(vertices, int):
            super().__init__(vertices, directed)

        else:
            raise TypeError("Invalid constructor arguments")

    # ---------- EDGE OPERATIONS ---------- #

    def add_edge(self, u: int, v: int) -> None:
        """
        Add an edge between two vertices.

        Parameters
        ----------
        u : int
            Source vertex
        v : int
            Destination vertex

        Raises
        ------
        TypeError
            If inputs are not integers

        ValueError
            If indices are negative
        """
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("u and v must be integers")

        if u < 0 or v < 0:
            raise ValueError("Node indices must be non-negative")

        super().add_edge(u, v)

    def add_edges(self, edges: Iterable[Tuple[int, int]]) -> None:
        """
        Add multiple edges.

        Parameters
        ----------
        edges : Iterable[Tuple[int, int]]
            Collection of edges (u, v)
        """
        for u, v in edges:
            self.add_edge(u, v)

    def add_vertex(self) -> None:
        """
        Add a new vertex to the graph.

        The new vertex will have no edges initially.
        """
        super().add_vertex()

    # ---------- BUILD ---------- #

    def build_from_adj_matrix(self, matrix: List[List[int]]) -> None:
        """
        Build graph from adjacency matrix.

        Parameters
        ----------
        matrix : List[List[int]]
            Square matrix where matrix[i][j] = 1 indicates edge
        """
        super().build_from_adj_matrix(matrix)

    def build_from_adj_list(self, adjacency: List[List[int]]) -> None:
        """
        Build graph from adjacency list.

        Parameters
        ----------
        adjacency : List[List[int]]
            adjacency[i] contains neighbors of node i
        """
        super().build_from_adj_list(adjacency)

    # ---------- GRAPH INFO ---------- #

    def vertices(self) -> int:
        """
        Get number of vertices.

        Returns
        -------
        int
        """
        return super().vertices()

    def is_directed(self) -> bool:
        """
        Check if graph is directed.

        Returns
        -------
        bool
        """
        return super().is_directed()

    def get_adj(self) -> List[List[int]]:
        """
        Get adjacency list.

        Returns
        -------
        List[List[int]]
        """
        return super().get_adj()

    def degree(self, u: int) -> int:
        """
        Get degree of a vertex.

        Parameters
        ----------
        u : int

        Returns
        -------
        int
        """
        return super().degree(u)

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if edge exists.

        Parameters
        ----------
        u : int
        v : int

        Returns
        -------
        bool
        """
        return super().has_edge(u, v)

    # ---------- DEBUG ---------- #

    def print_graph(self) -> None:
        """
        Print graph structure (for debugging).
        """
        super().print_graph()

    # ---------- UTIL ---------- #

    def __repr__(self) -> str:
        return f"Graph(vertices={self.vertices()}, directed={self.is_directed()})"


# ================= WEIGHTED GRAPH ================= #
class WeightedGraph(_WeightedGraph):
    """
    Weighted graph data structure.

    This extends the Graph class by associating weights with edges.

    Notes
    -----
    - Edge weights are stored as float
    - Supports directed and undirected graphs
    """

    def __init__(self, vertices: int, directed: bool = False) -> None:
        """
        Initialize weighted graph.

        Parameters
        ----------
        vertices : int
            Number of vertices

        directed : bool, default=False

        Raises
        ------
        ValueError
            If vertices is invalid
        """
        if not isinstance(vertices, int) or vertices <= 0:
            raise ValueError("vertices must be a positive integer")

        super().__init__(vertices, directed)

    # ---------- EDGE OPERATIONS ---------- #

    def add_edge(self, u: int, v: int, w: float) -> None:
        """
        Add weighted edge.

        Parameters
        ----------
        u : int
        v : int
        w : float
            Edge weight

        Raises
        ------
        TypeError
            If invalid types
        """
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("u and v must be integers")

        if not isinstance(w, (int, float)):
            raise TypeError("weight must be numeric")

        if u < 0 or v < 0:
            raise ValueError("Node indices must be non-negative")

        super().add_edge(u, v, float(w))

    def add_edges(self, edges: Iterable[Tuple[int, int, float]]) -> None:
        """
        Add multiple weighted edges.

        Parameters
        ----------
        edges : Iterable[Tuple[int, int, float]]
        """
        for u, v, w in edges:
            self.add_edge(u, v, w)

    def add_vertex(self) -> None:
        """
        Add new vertex.
        """
        super().add_vertex()

    # ---------- BUILD ---------- #

    def build_from_adj_list(
        self,
        adjacency: List[List[Tuple[int, float]]],
    ) -> None:
        """
        Build graph from weighted adjacency list.

        Parameters
        ----------
        adjacency : List[List[Tuple[int, float]]]
        """
        super().build_from_adj_list(adjacency)

    def build_from_adj_matrix(
        self,
        matrix: List[List[float]],
    ) -> None:
        """
        Build graph from weighted adjacency matrix.

        Parameters
        ----------
        matrix : List[List[float]]
        """
        super().build_from_adj_matrix(matrix)

    # ---------- GRAPH INFO ---------- #

    def vertices(self) -> int:
        """Return number of vertices."""
        return super().vertices()

    def is_directed(self) -> bool:
        """Check if graph is directed."""
        return super().is_directed()

    def get_adj(self) -> List[List[Tuple[int, float]]]:
        """
        Get weighted adjacency list.

        Returns
        -------
        List[List[Tuple[int, float]]]
        """
        return super().get_adj()

    def degree(self, u: int) -> int:
        """Return degree of vertex."""
        return super().degree(u)

    def has_edge(self, u: int, v: int) -> bool:
        """Check if edge exists."""
        return super().has_edge(u, v)

    # ---------- DEBUG ---------- #

    def print_graph(self) -> None:
        """Print weighted graph."""
        super().print_graph()

    # ---------- UTIL ---------- #

    def __repr__(self) -> str:
        return f"WeightedGraph(vertices={self.vertices()}, directed={self.is_directed()})"