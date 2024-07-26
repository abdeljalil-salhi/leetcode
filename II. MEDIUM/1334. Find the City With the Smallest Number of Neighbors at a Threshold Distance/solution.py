class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        def dijkstra(source: int) -> int:
            heap = [(0, source)]
            visited = set()

            while heap:
                weight, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)

                for neighbor, _weight in adjs[node]:
                    neighborWeight = weight + _weight
                    if neighborWeight <= distanceThreshold:
                        heapq.heappush(heap, (neighborWeight, neighbor))

            return len(visited) - 1

        adjs = defaultdict(list)

        for _from, _to, _weight in edges:
            adjs[_from].append((_to, _weight))
            adjs[_to].append((_from, _weight))

        result, minimum = -1, n
        for source in range(n):
            count = dijkstra(source)
            if count <= minimum:
                result = source
                minimum = count

        return result
