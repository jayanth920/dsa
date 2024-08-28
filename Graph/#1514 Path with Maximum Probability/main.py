import heapq
from collections import defaultdict

def maxProbability(n, edges, succProb, start_node, end_node):
        # Build thye graph
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Max heap: start with (-probability, start_node)
        max_heap = [(-1, start_node)]
        probabilities = [0] * n
        probabilities[start_node] = 1  # The probability to start node is 1

        while max_heap:
            # Get the node with the highest probability
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob

            # If we reach the end node, return the probability
            if node == end_node:
                return curr_prob

            # Visit each neighbor
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                # If we found a path with a higher probability, update and push to the heap
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        # If there's no path from start to end
        return 0.0