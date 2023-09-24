import sys
import random
import heapq

def generate_sparse_graph(num_nodes):
    # Generate a sparse graph with random edge weights
    graph = {}
    for i in range(num_nodes):
        graph[i] = [(j, random.randint(1, 100)) for j in range(num_nodes) if i != j]
    return graph

def prim_mst_eager_sparse(graph):
    num_nodes = len(graph)
    # Initialize data structures to keep track of the MST
    mst = []  # Stores the edges of the MST
    key = [sys.maxsize] * num_nodes  # Key values to track minimum edge weights
    parent = [-1] * num_nodes  # Parent array to construct MST
    in_mst = [False] * num_nodes  # Track nodes in MST
    heap = [(0, 0)]  # Priority queue to store candidate edges (weight, node)

    while heap:
        weight, node = heapq.heappop(heap)

        # If the node is already in the MST, skip it
        if in_mst[node]:
            continue

        in_mst[node] = True
        if parent[node] != -1:
            mst.append((parent[node], node, weight))

        # Update key values and push adjacent nodes to the heap
        for neighbor, edge_weight in graph[node]:
            if not in_mst[neighbor] and edge_weight < key[neighbor]:
                key[neighbor] = edge_weight
                parent[neighbor] = node
                heapq.heappush(heap, (key[neighbor], neighbor))

    return mst

# Define the number of nodes for the sparse graph (5000 nodes)
num_nodes_sparse = 5000

# Generate a sparse graph with random edge weights
graph_sparse = generate_sparse_graph(num_nodes_sparse)

# Find the MST and print the result
mst_edges_sparse = prim_mst_eager_sparse(graph_sparse)
print("Minimum Spanning Tree Edges (Eager Sparse Graph - 5000 nodes, Sample of 10 edges):")
sample_size = 10  # Adjust this value to change the sample size
for edge in mst_edges_sparse[:sample_size]:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")