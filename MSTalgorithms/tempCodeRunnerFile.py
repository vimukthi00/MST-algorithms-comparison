    def relax_edges_at_node(self, current_node_index: int):
        self.visited[current_node_index] = True
        edges = self.graph[current_node_index]

        for edge in edges:
            dest_node_index = edge.to_node

            if self.visited[dest_node_index]:
                continue

            if self.ipq.contains(dest_node_index):  # Check if dest_node_index is in the IPQ.
                # Try to improve the cheapest edge at dest_node_index with the current edge in the IPQ.
                self.ipq.decrease(dest_node_index, edge)
            else:
                # Insert edge for the first time.
                self.ipq.insert(dest_node_index, edge)

