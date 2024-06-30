class UnionFind:

    def __init__(self, n: int):
        self.n = n
        self.parent = {}
        self.rank = {}
        for i in range(n + 1):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, n: int) -> int:
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1: int, n2: int) -> int:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.n -= 1

        return 1

    def isConnected(self) -> bool:
        return self.n == 1


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        keep = 0

        for t, u, v in edges:
            if t == 3 and (alice.union(u, v) and bob.union(u, v)):
                keep += 1

        for t, u, v in edges:
            if t == 1:
                keep += alice.union(u, v)
            elif t == 2:
                keep += bob.union(u, v)

        if alice.isConnected() and bob.isConnected():
            return len(edges) - keep

        return -1
