class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adjs = defaultdict(list)
        visitTimes = defaultdict(list)

        for U, V in edges:
            adjs[U].append(V)
            adjs[V].append(U)

        deq = deque([1])
        currentTime, result = 0, -1

        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()

                if node == n:
                    if result != -1:
                        return currentTime
                    result = currentTime

                for neighbor in adjs[node]:
                    neighborVisitTimes = visitTimes[neighbor]
                    if not len(neighborVisitTimes) or (
                        len(neighborVisitTimes) == 1
                        and neighborVisitTimes[0] != currentTime
                    ):
                        deq.append(neighbor)
                        neighborVisitTimes.append(currentTime)

            if (currentTime // change) % 2:
                currentTime += change - (currentTime % change)
            currentTime += time
