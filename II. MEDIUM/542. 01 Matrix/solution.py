class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        deq, distance = deque(), []

        ROWS, COLS = len(mat), len(mat[0])
        for i in range(ROWS):
            distance.append([])
            for j in range(COLS):
                if mat[i][j] == 0:
                    deq.append((i, j))
                    distance[i].append(0)
                else:
                    distance[i].append(10001)  # max constraint plus one

        while deq:
            i, j = deq.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row, col = i + di, j + dj
                if 0 <= row < ROWS and 0 <= col < COLS:
                    if distance[row][col] > distance[i][j] + 1:
                        distance[row][col] = distance[i][j] + 1
                        deq.append((row, col))

        return distance
