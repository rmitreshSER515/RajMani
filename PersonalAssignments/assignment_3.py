# -*- coding: utf-8 -*-
"""
SER501 Assignment 3 scaffolding code
created by: Xiangyu Guo
"""
import sys
import math
import heapq
# =============================================================================


class Graph(object):
    """docstring for Graph"""
    user_defined_vertices = []
    dfs_timer = 0

    def __init__(self, vertices, edges):
        super(Graph, self).__init__()
        n = len(vertices)
        self.matrix = [[0 for x in range(n)] for y in range(n)]
        self.vertices = vertices
        self.edges = edges
        for edge in edges:
            x = vertices.index(edge[0])
            y = vertices.index(edge[1])
            self.matrix[x][y] = edge[2]

    def display(self):
        print(self.vertices)
        for i, v in enumerate(self.vertices):
            print(v, self.matrix[i])
    
    def print_d_and_pi(self, iteration, d, pi):
        assert ((len(d) == len(self.vertices)) and
               (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            val = 'inf' if d[i] == sys.maxsize else d[i]
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, val, pi[i]))

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix))]
        self.matrix = transposed_matrix

    def in_degree(self):
        degree = [0] * len(self.vertices)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                degree[i] += self.matrix[j][i]
        self.print_degree(degree)

    def out_degree(self):
        out_degrees = [0] * len(self.vertices)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                out_degrees[i] += self.matrix[i][j]
        self.print_degree(out_degrees)

    def dfs_visit(self, u, color, discovery, finish):

        color[u] = "GREY"
        self.dfs_timer += 1
        discovery[u] = self.dfs_timer
        # Visit all adjacent vertices
        for v in range(len(self.vertices)):
            if self.matrix[u][v] != 0 and color[v] == "WHITE":
                self.dfs_visit(v, color, discovery, finish)
        color[u] = "BLACK"
        self.dfs_timer += 1
        finish[u] = self.dfs_timer

    def dfs_on_graph(self):
        self.dfs_timer = 0
        discovery = [-1] * len(self.vertices)
        finish = [-1] * len(self.vertices)
        color = ["WHITE"] * len(self.vertices)  # WHITE: unvisited, GREY: visiting, BLACK: visited
        for u in range(len(self.vertices)):
            if color[u] == "WHITE":
                self.dfs_visit(u, color, discovery, finish)
        self.print_discover_and_finish_time(discovery, finish)

    def prim(self, root):
        n = len(self.vertices)
        key = [math.inf] * n  # Keys to pick minimum weight edge
        parent = [None] * n  
        in_mst = [False] * n
        root_index = self.vertices.index(root)
        key[root_index] = 0
        min_heap = [(0, root_index)] 
        self.print_d_and_pi("Initial", key, parent)
        iteration = 0
        while min_heap:
            _, u = heapq.heappop(min_heap)
            if in_mst[u]:
                continue
            in_mst[u] = True

            # Iterate over all vertices adjacent to u
            for v in range(n):
                weight = self.matrix[u][v]
                if weight != 0 and not in_mst[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = self.vertices[u]
                    heapq.heappush(min_heap, (key[v], v))
            self.print_d_and_pi(iteration, key, parent)
            iteration += 1

    def bellman_ford(self, source):
        n = len(self.vertices)
        d = [math.inf] * n  # Distance array initialized to infinity
        pi = [None] * n  
        source_index = self.vertices.index(source)
        d[source_index] = 0  
        self.print_d_and_pi("Initial", d, pi)

        for i in range(n - 1):
            for edge in self.edges:
                u = self.vertices.index(edge[0])
                v = self.vertices.index(edge[1])
                weight = edge[2]
                if d[u] != math.inf and d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    pi[v] = self.vertices[u]
            self.print_d_and_pi(i + 1, d, pi)

    def dijkstra(self, source):
        n = len(self.vertices)
        d = [math.inf] * n  # Distance array, initialized to infinity
        pi = [None] * n
        source_index = self.vertices.index(source)
        d[source_index] = 0  # Distance to the source is 0
        Q = [(0, source_index)]  # Priority queue initialized with the source
        self.print_d_and_pi("Initial", d, pi)
        iteration_count = 0
        while Q:
            _, u = heapq.heappop(Q)

            for v in range(n):
                weight = self.matrix[u][v]
                if weight != 0 and d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    pi[v] = self.vertices[u]
                    heapq.heappush(Q, (d[v], v))
            iteration_count += 1
            self.print_d_and_pi(iteration_count, d, pi)

    def print_discover_and_finish_time(self, discover, finish):
        assert ((len(discover) == len(self.vertices)) and
               (len(finish) == len(self.vertices)))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\tDiscovered: {1}\tFinished: {2}".format(
                    v, discover[i], finish[i]))

    def print_degree(self, degree):
        assert ((len(degree) == len(self.vertices)))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\tDegree: {1}".format(v, degree[i]))


def main():
    # Thoroughly test your program and produce useful output.
    # Q1 and Q2
    graph = Graph(['1', '2'], [('1', '2', 1)])
    graph.display()
    graph.transpose()
    graph.display()
    graph.transpose()
    graph.display()
    graph.in_degree()
    graph.out_degree()
    graph.print_d_and_pi(1, [1, sys.maxsize], [2, None])
    graph.print_degree([1, 0])
    graph.print_discover_and_finish_time([0, 2], [1, 3])

    # Q3
    graph = Graph(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                  [('q', 's', 1),
                   ('s', 'v', 1),
                   ('v', 'w', 1),
                   ('w', 's', 1),
                   ('q', 'w', 1),
                   ('q', 't', 1),
                   ('t', 'x', 1),
                   ('x', 'z', 1),
                   ('z', 'x', 1),
                   ('t', 'y', 1),
                   ('y', 'q', 1),
                   ('r', 'y', 1),
                   ('r', 'u', 1),
                   ('u', 'y', 1)])
    print("DFS ON GRAPH")
    graph.display()
    graph.dfs_on_graph()

    # Q4 - Prim
    graph = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                  [('A', 'H', 6),
                   ('H', 'A', 6),
                   ('A', 'B', 4),
                   ('B', 'A', 4),
                   ('B', 'H', 5),
                   ('H', 'B', 5),
                   ('B', 'C', 9),
                   ('C', 'B', 9),
                   ('G', 'H', 14),
                   ('H', 'G', 14),
                   ('F', 'H', 10),
                   ('H', 'F', 10),
                   ('B', 'E', 2),
                   ('E', 'B', 2),
                   ('G', 'F', 3),
                   ('F', 'G', 3),
                   ('E', 'F', 8),
                   ('F', 'E', 8),
                   ('D', 'E', 15),
                   ('E', 'D', 15)])
    print("Prim's Algorithm")
    graph.prim('G')

    # Q5
    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('t', 'x', 5),
                   ('t', 'y', 8),
                   ('t', 'z', -4),
                   ('x', 't', -2),
                   ('y', 'x', -3),
                   ('y', 'z', 9),
                   ('z', 'x', 7),
                   ('z', 's', 2),
                   ('s', 't', 6),
                   ('s', 'y', 7)])
    print("Bellman ford algorithm")
    graph.bellman_ford('z')

    # Q5 alternate
    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('t', 'x', 5),
                   ('t', 'y', 8),
                   ('t', 'z', -4),
                   ('x', 't', -2),
                   ('y', 'x', -3),
                   ('y', 'z', 9),
                   ('z', 'x', 4),
                   ('z', 's', 2),
                   ('s', 't', 6),
                   ('s', 'y', 7)])
    print("Bellman ford algorithm 2")
    graph.bellman_ford('s')

    # Q6
    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('s', 't', 3),
                   ('s', 'y', 5),
                   ('t', 'x', 6),
                   ('t', 'y', 2),
                   ('x', 'z', 2),
                   ('y', 't', 1),
                   ('y', 'x', 4),
                   ('y', 'z', 6),
                   ('z', 's', 3),
                   ('z', 'x', 7)])
    print("Dijiktras algorithm")
    graph.dijkstra('s')


if __name__ == '__main__':
    main()