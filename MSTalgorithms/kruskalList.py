import random
import networkx as nx

# Create an empty graph
graph = nx.Graph()

# Add nodes to the graph
num_nodes = 10
graph.add_nodes_from(range(num_nodes))

# Generate random edges
num_edges = 15
edges = []
for _ in range(num_edges):
    u = random.randint(0, num_nodes - 1)
    v = random.randint(0, num_nodes - 1)
    edges.append((u, v))

# Add edges to the graph
graph.add_edges_from(edges)

# Print the adjacency list
adj_list = graph.adjacency()
for node, neighbors in adj_list:
    print(f"Node {node}: {list(neighbors)}")


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

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
        for u in self.adj_list:
            for v in self.adj_list[u]:
                edges.append((u, v))

        for edge in edges:
            u, v = edge
            u_root = self.find(parent, u)
            v_root = self.find(parent, v)

            if u_root != v_root:
                mst.append(edge)
                self.union(parent, rank, u_root, v_root)

        return mst


# Create a graph object
g = Graph(num_nodes)

# Add edges to the graph
for edge in edges:
    u, v = edge
    g.add_edge(u, v)

# Run Kruskal's algorithm
mst = g.kruskal()

# Print the minimum spanning tree edges
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)


# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = []

#     def add_edge(self, u, v, w):
#         self.graph.append([u, v, w])

#     # to find the parent of a given node
#     def find(self, parent, i):
#         if parent[i] == i:
#             return i
#         return self.find(parent, parent[i])

#     # find the union of two sets
#     def union(self, parent, rank, x, y):
#         root_x = self.find(parent, x)
#         root_y = self.find(parent, y)

#         if rank[root_x] < rank[root_y]:
#             parent[root_x] = root_y
#         elif rank[root_x] > rank[root_y]:
#             parent[root_y] = root_x
#         else:
#             parent[root_y] = root_x
#             rank[root_x] += 1

#     def kruskal(self):
#         result = []
#         parent = []
#         rank = []

#         i = 0
#         e = 0

#         self.graph = sorted(self.graph, key=lambda item: item[2])

#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)

#         while e < self.V - 1:
#             u, v, w = self.graph[i]
#             i = i + 1
#             x = self.find(parent, u)
#             y = self.find(parent, v)

#             if x != y:
#                 e = e + 1
#                 result.append([u, v, w])
#                 self.union(parent, rank, x, y)

#         print("Edges in the MST:")
#         for u, v, weight in result:
#             print(f"{u} -- {v} == {weight}")


# g = Graph(4)
# g.add_edge(0, 1, 10)
# g.add_edge(0, 2, 6)
# g.add_edge(0, 3, 5)
# g.add_edge(1, 3, 15)
# g.add_edge(2, 3, 4)

# mst = g.kruskal()

# # g.add_edge(0, 1, 4)
# # g.add_edge(0, 7, 8)
# # g.add_edge(1, 7, 11)
# # g.add_edge(1, 2, 8)
# # g.add_edge(2, 8, 2)
# # g.add_edge(7, 8, 7)
# # g.add_edge(6, 7, 1)
# # g.add_edge(7, 8, 7)
# # g.add_edge(6, 8, 6)
# # g.add_edge(2, 5, 4)
# # g.add_edge(6, 5, 2)
# # g.add_edge(2, 3, 7)
# # g.add_edge(3, 4, 9)
# # g.add_edge(3, 5, 14)
# # g.add_edge(5, 4, 10)
