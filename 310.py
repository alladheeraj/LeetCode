from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # base cases
        if n <= 1:
            return [0]
        if n == 2:
            return [0, 1]

        # build graph and initialize degrees array
        graph = defaultdict(list)
        degrees = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # initialize queue with leaf nodes
        leaves = deque()
        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)

        # repeatedly remove leaf nodes until 1 or 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            for i in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)

        # remaining nodes are the root(s) of the minimum height tree(s)
        return list(leaves)
