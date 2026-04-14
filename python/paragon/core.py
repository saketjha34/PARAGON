from __future__ import annotations
from typing import List, Tuple, Iterable, Optional, Union

from ._paragon import Graph as _Graph
from ._paragon import WeightedGraph as _WeightedGraph


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
            self._validate_adj_list(vertices)
            super().__init__(vertices, directed)

        elif isinstance(vertices, int) and edges is not None:
            self._validate_vertex_count(vertices)
            self._validate_edges(edges, vertices)
            super().__init__(vertices, list(edges), directed)

        elif isinstance(vertices, int):
            self._validate_vertex_count(vertices)
            super().__init__(vertices, directed)

        else:
            raise TypeError("Invalid constructor arguments")

    # ================= INTERNAL VALIDATION ================= #

    def _validate_vertex_count(self, v: int) -> None:
        if not isinstance(v, int):
            raise TypeError("vertices must be an integer")
        if v <= 0:
            raise ValueError("vertices must be a positive integer")

    def _validate_node(self, u: int) -> None:
        if not isinstance(u, int):
            raise TypeError("node index must be an integer")
        if u < 0 or u >= self.vertices():
            raise ValueError(f"Invalid node index: {u}")

    def _validate_edge(self, u: int, v: int) -> None:
        self._validate_node(u)
        self._validate_node(v)

    def _validate_edges(self, edges, max_v: int) -> None:
        for e in edges:
            if not isinstance(e, tuple) or len(e) != 2:
                raise TypeError("edges must be tuples of (u, v)")

            u, v = e
            if not isinstance(u, int) or not isinstance(v, int):
                raise TypeError("edge vertices must be integers")

            if u < 0 or v < 0 or u >= max_v or v >= max_v:
                raise ValueError(f"Invalid edge ({u}, {v})")

    def _validate_adj_list(self, adj: List[List[int]]) -> None:
        if not isinstance(adj, list):
            raise TypeError("adjacency must be a list of lists")

        n = len(adj)

        for i, neighbors in enumerate(adj):
            if not isinstance(neighbors, list):
                raise TypeError("each adjacency entry must be a list")

            for v in neighbors:
                if not isinstance(v, int):
                    raise TypeError("adjacency values must be integers")

                if v < 0 or v >= n:
                    raise ValueError(f"Invalid adjacency entry {v} at node {i}")

    def _validate_matrix(self, matrix: List[List[int]]) -> None:
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a list of lists")

        n = len(matrix)

        for row in matrix:
            if not isinstance(row, list) or len(row) != n:
                raise ValueError("matrix must be square")

            for val in row:
                if not isinstance(val, int):
                    raise TypeError("matrix values must be integers")

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

        self._validate_edge(u, v)
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
        self._validate_matrix(matrix)
        super().build_from_adj_matrix(matrix)

    def build_from_adj_list(self, adjacency: List[List[int]]) -> None:
        """
        Build graph from adjacency list.

        Parameters
        ----------
        adjacency : List[List[int]]
            adjacency[i] contains neighbors of node i
        """
        self._validate_adj_list(adjacency)
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
        self._validate_node(u)
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
        self._validate_edge(u, v)
        return super().has_edge(u, v)

    # ---------- DEBUG ---------- #

    def print_graph(self) -> None:
        """
        Print graph structure (for debugging).
        """
        super().print_graph()


    # ---------- UTIL ---------- #
    def __repr__(self) -> str:
        """
        Return developer-friendly string representation of the graph.

        Includes number of vertices, edges, and graph type.

        Returns
        -------
        str
        """
        return (
            f"Graph(vertices={self.vertices()}, "
            f"edges={sum(len(x) for x in self.get_adj())}, "
            f"directed={self.is_directed()})"
        )

    def __len__(self) -> int:
        """
        Return number of vertices in the graph.

        Enables usage of len(graph).

        Returns
        -------
        int
        """
        return self.vertices()

    def __contains__(self, node: int) -> bool:
        """
        Check if a node exists in the graph.

        Enables usage like: node in graph

        Parameters
        ----------
        node : int

        Returns
        -------
        bool
        """
        return isinstance(node, int) and 0 <= node < self.vertices()

    def __getitem__(self, node: int):
        """
        Get neighbors of a node.

        Enables usage like: graph[node]

        Parameters
        ----------
        node : int

        Returns
        -------
        List[int]
        """
        self._validate_node(node)
        return self.get_adj()[node]

    def __iter__(self):
        """
        Iterate over graph nodes.

        Enables usage like: for node in graph

        Returns
        -------
        iterator
        """
        return iter(range(self.vertices()))

    def __eq__(self, other) -> bool:
        """
        Compare two graphs for equality.

        Two graphs are equal if:
        - Same number of vertices
        - Same adjacency list
        - Same directed property

        Parameters
        ----------
        other : Graph

        Returns
        -------
        bool
        """
        if not isinstance(other, Graph):
            return False

        return (
            self.vertices() == other.vertices()
            and self.is_directed() == other.is_directed()
            and self.get_adj() == other.get_adj()
        )

    def __ne__(self, other) -> bool:
        """
        Check if two graphs are not equal.

        Parameters
        ----------
        other : Graph

        Returns
        -------
        bool
        """
        return not self.__eq__(other)

    def __bool__(self) -> bool:
        """
        Check if graph is non-empty.

        Enables usage like: if graph:

        Returns
        -------
        bool
        """
        return self.vertices() > 0

    def __copy__(self):
        """
        Create a shallow copy of the graph.

        Returns
        -------
        Graph
        """
        return Graph(self.get_adj(), directed=self.is_directed())

    def __deepcopy__(self, memo):
        """
        Create a deep copy of the graph.

        Parameters
        ----------
        memo : dict

        Returns
        -------
        Graph
        """
        return Graph(
            [list(neigh) for neigh in self.get_adj()],
            directed=self.is_directed()
        )
        

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

    # ================= INTERNAL VALIDATION ================= #

    def _validate_node(self, u: int) -> None:
        if not isinstance(u, int):
            raise TypeError("node index must be an integer")
        if u < 0 or u >= self.vertices():
            raise ValueError(f"Invalid node index: {u}")

    def _validate_edge(self, u: int, v: int) -> None:
        self._validate_node(u)
        self._validate_node(v)

    def _validate_weight(self, w: float) -> None:
        if not isinstance(w, (int, float)):
            raise TypeError("weight must be numeric")

    def _validate_adj_list(self, adjacency):
        if not isinstance(adjacency, list):
            raise TypeError("adjacency must be a list of lists")

        n = len(adjacency)

        for i, neighbors in enumerate(adjacency):
            if not isinstance(neighbors, list):
                raise TypeError("each adjacency entry must be a list")

            for item in neighbors:
                if not isinstance(item, tuple) or len(item) != 2:
                    raise TypeError("adjacency must contain (node, weight) tuples")

                v, w = item

                if not isinstance(v, int):
                    raise TypeError("node index must be integer")

                if v < 0 or v >= n:
                    raise ValueError(f"Invalid node index {v} at node {i}")

                if not isinstance(w, (int, float)):
                    raise TypeError("weight must be numeric")

    def _validate_matrix(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a list of lists")

        n = len(matrix)

        for row in matrix:
            if not isinstance(row, list) or len(row) != n:
                raise ValueError("matrix must be square")

            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("matrix values must be numeric")

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

        self._validate_edge(u, v)
        self._validate_weight(w)

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
        self._validate_adj_list(adjacency)
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
        self._validate_matrix(matrix)
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
        self._validate_node(u)
        return super().degree(u)

    def has_edge(self, u: int, v: int) -> bool:
        """Check if edge exists."""
        self._validate_edge(u, v)
        return super().has_edge(u, v)

    # ---------- DEBUG ---------- #

    def print_graph(self) -> None:
        """Print weighted graph."""
        super().print_graph()

    # ---------- UTIL (DUNDER METHODS) ---------- #

    def __repr__(self) -> str:
        """
        Return developer-friendly string representation.

        Returns
        -------
        str
        """
        return (
            f"WeightedGraph(vertices={self.vertices()}, "
            f"edges={sum(len(x) for x in self.get_adj())}, "
            f"directed={self.is_directed()})"
        )

    def __len__(self) -> int:
        """
        Return number of vertices.

        Returns
        -------
        int
        """
        return self.vertices()

    def __contains__(self, node: int) -> bool:
        """
        Check if node exists.

        Parameters
        ----------
        node : int

        Returns
        -------
        bool
        """
        return isinstance(node, int) and 0 <= node < self.vertices()

    def __getitem__(self, node: int):
        """
        Get neighbors of node.

        Parameters
        ----------
        node : int

        Returns
        -------
        List[Tuple[int, float]]
        """
        self._validate_node(node)
        return self.get_adj()[node]

    def __iter__(self):
        """
        Iterate over nodes.

        Returns
        -------
        iterator
        """
        return iter(range(self.vertices()))

    def __eq__(self, other) -> bool:
        """
        Compare graphs.

        Returns
        -------
        bool
        """
        if not isinstance(other, WeightedGraph):
            return False

        return (
            self.vertices() == other.vertices()
            and self.is_directed() == other.is_directed()
            and self.get_adj() == other.get_adj()
        )

    def __ne__(self, other) -> bool:
        """
        Check inequality.

        Returns
        -------
        bool
        """
        return not self.__eq__(other)

    def __bool__(self) -> bool:
        """
        Check if graph is non-empty.

        Returns
        -------
        bool
        """
        return self.vertices() > 0

    def __copy__(self):
        """
        Shallow copy.

        Returns
        -------
        WeightedGraph
        """
        return WeightedGraph(self.vertices(), directed=self.is_directed())

    def __deepcopy__(self, memo):
        """
        Deep copy.

        Returns
        -------
        WeightedGraph
        """
        new_graph = WeightedGraph(self.vertices(), directed=self.is_directed())
        new_graph.build_from_adj_list(
            [[(v, w) for v, w in neighbors] for neighbors in self.get_adj()]
        )
        return new_graph