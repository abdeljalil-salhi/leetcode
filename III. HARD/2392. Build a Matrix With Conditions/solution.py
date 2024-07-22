class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topologicalSort(edges):
            adjs = defaultdict(list)
            for src, dst in edges:
                adjs[src].append(dst)

            visited, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adjs, visited, path, order):
                    return []

            return order[::-1]

        def dfs(src, adjs, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True

            visited.add(src)
            path.add(src)

            for edge in adjs[src]:
                if not dfs(edge, adjs, visited, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        row_sorted = topologicalSort(rowConditions)
        col_sorted = topologicalSort(colConditions)

        if not row_sorted or not col_sorted:
            return []

        matrix = [[0] * k for _ in range(k)]

        row_values = {n: i for i, n in enumerate(row_sorted)}
        col_values = {n: i for i, n in enumerate(col_sorted)}
        for n in range(1, k + 1):
            row, col = row_values[n], col_values[n]
            matrix[row][col] = n

        return matrix
