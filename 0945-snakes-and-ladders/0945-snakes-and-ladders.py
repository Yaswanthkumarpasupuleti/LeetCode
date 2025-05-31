from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        def get_coordinates(pos):
            r, c = divmod(pos - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        dist = {1: 0}
        queue = deque([1])

        while queue:
            pos = queue.popleft()
            for move in range(1, 7):
                next_pos = pos + move
                if next_pos > n * n:
                    continue
                r, c = get_coordinates(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos not in dist or dist[next_pos] > dist[pos] + 1:
                    dist[next_pos] = dist[pos] + 1
                    queue.append(next_pos)

        return dist.get(n * n, -1)