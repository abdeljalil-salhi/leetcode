class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deq = deque()
        adj, visited = [], []

        for _ in range(numCourses):
            adj.append([])
            visited.append(0)

        def topoSortHelper(i: int) -> bool:
            if visited[i] == 1:
                return False
            elif visited[i] == 2:
                return True

            visited[i] = 1
            for j in adj[i]:
                if not topoSortHelper(j):
                    return False
            visited[i] = 2
            deq.appendleft(i)
            return True

        def topoSort() -> bool:
            for i in range(numCourses):
                if not visited[i]:
                    if not topoSortHelper(i):
                        return False
            return True

        for edge in prerequisites:
            adj[edge[0]].append(edge[1])

        return topoSort()
