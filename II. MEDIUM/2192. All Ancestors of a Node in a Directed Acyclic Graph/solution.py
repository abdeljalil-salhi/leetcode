class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        deq = deque()
        adj, visited, ancestors = [], [], []

        for _ in range(n):
            adj.append([])
            ancestors.append(set())
            visited.append(0)

        def topoSortHelper(i: int) -> None:
            visited[i] += 1
            for j in adj[i]:
                if not visited[j]:
                    topoSortHelper(j)
            deq.appendleft(i)

        def topoSort() -> None:
            for i in range(n):
                if not visited[i]:
                    topoSortHelper(i)

        for edge in edges:
            adj[edge[0]].append(edge[1])

        topoSort()

        while deq:
            node = deq.popleft()
            for neighbor in adj[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

        return [sorted(list(ancestor)) for ancestor in ancestors]
