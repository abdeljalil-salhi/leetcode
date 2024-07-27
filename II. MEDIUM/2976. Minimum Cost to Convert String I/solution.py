class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        totalCost = 0

        def dijkstra(_source):
            heap = [(0, _source)]
            minimumCostMap = {}

            while heap:
                cost, node = heapq.heappop(heap)

                if node in minimumCostMap:
                    continue

                minimumCostMap[node] = cost

                for neighbor, neighborCost in adjs[node]:
                    heapq.heappush(heap, (neighborCost + cost, neighbor))

            return minimumCostMap

        adjs = defaultdict(list)
        for _source, _destination, _currentCost in zip(original, changed, cost):
            adjs[_source].append((_destination, _currentCost))

        minimumCostMaps = {c: dijkstra(c) for c in set(source)}

        for _source, _destination in zip(source, target):
            if _destination not in minimumCostMaps[_source]:
                return -1

            totalCost += minimumCostMaps[_source][_destination]

        return totalCost
