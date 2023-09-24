import sys
import random
import heapq

def generate_dense_graph(num_nodes):
    # Generate a dense graph with random edge weights
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 100)  # Random edge weight (adjust range as needed)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

def prim_mst_eager_dense(graph):
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
        for v in range(num_nodes):
            if not in_mst[v] and graph[node][v] < key[v]:
                key[v] = graph[node][v]
                parent[v] = node
                heapq.heappush(heap, (key[v], v))

    return mst

# Define the number of nodes for the dense graph (5000 nodes)
num_nodes_dense = 5000

# Generate a dense graph with random edge weights
graph_dense = generate_dense_graph(num_nodes_dense)

# Find the MST and print the result
mst_edges_dense = prim_mst_eager_dense(graph_dense)
print("Minimum Spanning Tree Edges (Eager Dense Graph - 5000 nodes, Sample of 10 edges):")
sample_size = 10  # Adjust this value to change the sample size
for edge in mst_edges_dense[:sample_size]:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")