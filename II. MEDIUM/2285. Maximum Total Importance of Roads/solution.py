class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        # Count the number of roads connected to each city
        edges = Counter()
        for i, j in roads:
            edges[i] += 1
            edges[j] += 1

        # Sort the cities by the number of roads connected to them
        edges = sorted(edges.values(), reverse=True)

        # Calculate the total importance
        total = 0
        for i, e in enumerate(edges):
            total += (n - i) * e

        # Return the total importance
        return total
