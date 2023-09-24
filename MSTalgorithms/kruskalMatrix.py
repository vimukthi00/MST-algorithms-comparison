import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Number of nodes
num_nodes = 10

# Generate a dense graph adjacency matrix with random edge weights between 0 and 9
dense_graph = np.random.randint(10, size=(num_nodes, num_nodes))

# Ensure the graph is undirected (symmetric adjacency matrix)
dense_graph = np.triu(dense_graph) + np.triu(dense_graph, k=1).T

# Set the diagonal to 0 (no self-loops)
np.fill_diagonal(dense_graph, 0)

# Create a graph from the adjacency matrix
graph = nx.from_numpy_array(dense_graph)


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = dense_graph

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        parent = [i for i in range(self.num_nodes)]
        rank = [0] * self.num_nodes
        mst = []

        edges = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.adj_matrix[i][j] != 0:
                    edges.append((i, j, self.adj_matrix[i][j]))

        edges.sort(key=lambda x: x[2])

        for edge in edges:
            u, v, weight = edge
            u_root = self.find(parent, u)
            v_root = self.find(parent, v)

            if u_root != v_root:
                mst.append(edge)
                self.union(parent, rank, u_root, v_root)

        return mst


# Create a graph object
g = Graph(num_nodes)

# Run Kruskal's algorithm
mst = g.kruskal()

# Print the minimum spanning tree edges
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []
        parent = []
        rank = []

        i = 0
        e = 0

        edges = []

        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] != 0:
                    edges.append([u, v, self.graph[u][v]])

        edges = sorted(edges, key=lambda item: item[2])

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


# Example usage
# g = Graph(4)
# g.add_edge(0, 1, 10)
# g.add_edge(0, 2, 6)
# g.add_edge(0, 3, 5)
# g.add_edge(1, 3, 15)
# g.add_edge(2, 3, 4)

# mst = g.kruskal()
# print("Edges in the Minimum Spanning Tree:")
# for u, v, weight in mst:
#     print(f"{u} -- {v} == {weight}")
