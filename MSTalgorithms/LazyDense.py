import numpy as np
import random
import heapq

# Number of nodes

num_nodes = 10

# Generate a dense graph adjacency matrix with random edge weights between 0 and 9
dense_graph = np.random.randint(10, size=(num_nodes, num_nodes))

# Ensure the graph is undirected (symmetric adjacency matrix)
dense_graph = np.triu(dense_graph) + np.triu(dense_graph, k=1).T

# Set the diagonal to 0 (no self-loops)
np.fill_diagonal(dense_graph, 0)

# Create both adjacency matrix and adjacency list representations


def adjacency_matrix_and_list(graph_matrix):
    adjacency_matrix = graph_matrix.copy()

    adjacency_list = {}
    num_nodes = len(graph_matrix)
    for node in range(num_nodes):
        neighbors = []
        for neighbor, weight in enumerate(graph_matrix[node]):
            if weight > 0:
                neighbors.append((neighbor, weight))
        adjacency_list[node] = neighbors

    return adjacency_matrix, adjacency_list


# Get both representations of the graph
adj_matrix, adj_list = adjacency_matrix_and_list(dense_graph)

# Print the adjacency matrix (print only a portion of it)
print("Adjacency Matrix:")
print(adj_matrix)

# Print the adjacency list (print only a portion of it)
print("\nAdjacency List:")
for node, neighbors in adj_list.items():
    print(f"Node {node}: {neighbors}")


def lazy_prim_matrix(adj_matrix):
    num_nodes = len(adj_matrix)
    mst = []  # Minimum Spanning Tree edges
    visited = [False] * num_nodes

    # Create a list to store edges with their weights
    edges = [(float('inf'), None)] * num_nodes

    # Initialize with an arbitrary node (e.g., 0)
    start_node = 0

    while True:
        visited[start_node] = True

        # Add eligible edges to the priority queue
        for end_node, weight in enumerate(adj_matrix[start_node]):
            if not visited[end_node] and weight < edges[end_node][0]:
                edges[end_node] = (weight, start_node)

        # Find the minimum-weight edge to add to MST
        min_weight, min_edge = float('inf'), None
        for node, (weight, parent) in enumerate(edges):
            if not visited[node] and weight < min_weight:
                min_weight, min_edge = weight, node

        if min_edge is None:
            # No more eligible edges to add
            break

        mst.append((min_edge, edges[min_edge][1]))
        start_node = min_edge

    # Calculate the total weight of MST
    total_weight = sum(edge[0] for edge in mst)

    return mst, total_weight


def lazy_prim_list(adj_list):
    num_nodes = len(adj_list)
    mst = []  # Minimum Spanning Tree edges
    visited = [False] * num_nodes

    # Create a priority queue to store edges with their weights
    edge_heap = []

    # Initialize with an arbitrary node (e.g., 0)
    start_node = 0

    def visit(node):
        visited[node] = True
        for neighbor, weight in adj_list[node]:
            if not visited[neighbor]:
                heapq.heappush(edge_heap, (weight, node, neighbor))

    visit(start_node)

    while edge_heap:
        weight, src, dest = heapq.heappop(edge_heap)
        if visited[dest]:
            continue
        mst.append((src, dest, weight))
        visit(dest)

    # Calculate the total weight of MST
    total_weight = sum(edge[2] for edge in mst)

    return mst, total_weight


minimum_spanning_tree_matrix, total_weight_matrix = lazy_prim_matrix(
    adj_matrix)
minimum_spanning_tree_list, total_weight_list = lazy_prim_list(adj_list)

print("Minimum Spanning Tree Edges in Matrix:")
for edge in minimum_spanning_tree_matrix:
    print(edge)

print("Total Weight of MST in Matrix:", total_weight_matrix)
print("-------------------------------------------------------\n")
print("Minimum Spanning Tree Edges in List:")
for edge in minimum_spanning_tree_list:
    print(edge)

print("Total Weight of MST in List:", total_weight_list)
