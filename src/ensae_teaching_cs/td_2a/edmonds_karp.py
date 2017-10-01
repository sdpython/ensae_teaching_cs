"""
@file
@brief Implements the `Edmonds-Karp algorithm <https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm>`_
inspired from Wikipedia (same page).
"""
import copy
import collections
from pyquickhelper.loghelper import noLOG


class EdmondsKarpGraph:
    """
    This class represents a directed graph using adjacency
    matrix representation.
    """

    def __init__(self, edges):
        """
        The graph is defined as a list of tuple (n1, n2, capacity).
        is the capacity of the graph.

        @param      edges       list of tuple (n1, n2, capacity)
        """
        graph = {}
        for n1, n2, capacity in edges:
            if n1 not in graph:
                graph[n1] = {}
            graph[n1][n2] = capacity
        self._graph = graph  # residual graph

    def bfs(self, graph, s, t, parent):
        '''
        Returns True if there is a path from source *s* to sink *t* in
        residual graph. Also fills *parent* to store the path.

        @param  graph   graph
        @param  s       node 1
        @param  t       node 2
        @param  parent  stores the path
        @return         boolean
        '''
        # Mark all the vertices as not visited
        visited = {}

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for node, val in graph[u].items():
                if (not visited.get(node, False)) and val > 0:
                    queue.append(node)
                    visited[node] = True
                    parent[node] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited.get(t, False)

    def edmonds_karp(self, source, sink, fLOG=noLOG, verbose=False,
                     update=None):
        """
        Returns the maximum flow from s to t in the given graph.

        @param      source      source of the flow
        @param      sink        destination of the flow
        @param      fLOG        logging function
        @param      verbose     more information
        @param      update      custom update function
        @return                 maximum flow

        The update function can take into account linked edges.
        the default version is:

        ::

            def update_default(graph, u, v, path_flow):
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
        """
        graph = copy.deepcopy(self._graph)
        # Add symmetry.
        add_edges = []
        for n1, forward in graph.items():
            for n2 in forward:
                if n2 not in graph or n1 not in graph[n2]:
                    add_edges.append((n2, n1))
        for n1, n2 in add_edges:
            if n1 not in graph:
                graph[n1] = {}
            if n2 not in graph[n1]:
                graph[n1][n2] = 0

        if verbose:
            ini = copy.deepcopy(graph)
            fLOG("---------")
            for k, v in sorted(graph.items()):
                for kk, vv in sorted(v.items()):
                    if ini[k][kk] > 0:
                        fLOG("  {0} -> {1} : {2:03f}".format(k, kk, vv))
            fLOG("---------")

        # This array is filled by BFS and to store path
        parent = {}

        max_flow = 0  # There is no flow initially

        def update_default(graph, u, v, path_flow):
            graph[u][v] -= path_flow
            graph[v][u] += path_flow

        if update is None:
            update = update_default

        # Augment the flow while there is path from source to sink
        iteration = 0
        while self.bfs(graph, source, sink, parent):
            iteration += 1
            if fLOG:
                fLOG("[edmonds_karp] max_flow={0}".format(max_flow))

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                update(graph, u, v, path_flow)
                v = parent[v]

        if iteration == 0:
            raise ValueError("No path can increase max_flow.")

        if verbose:
            fLOG("---------")
            for k, v in sorted(graph.items()):
                for kk, vv in sorted(v.items()):
                    if ini[k][kk] != vv and ini[k][kk] > 0:
                        fLOG(
                            "  {0} -> {1} : {2:03f} -- ini {3:03f}".format(k, kk, vv, ini[k][kk]))
            fLOG("---", max_flow)
        if fLOG:
            fLOG("[edmonds_karp] max_flow={0}".format(max_flow))
        return max_flow
