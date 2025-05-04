from typing import List
class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def build(level):
            if level == 0:
                return [[0]]  # Base case: 1x1 grid

            # Recursively get the smaller grid of size 2^(level-1)
            small = build(level - 1)
            size = len(small)  # Size of the small grid
            k = size * size     # Number of elements in one quadrant
            new_size = size * 2  # New grid is double in size

            # Create an empty grid of new_size
            grid = [[0 for _ in range(new_size)] for _ in range(new_size)]

            for i in range(size):
                for j in range(size):
                    val = small[i][j]
                    # Fill top-left (add 3*k)
                    grid[i][j] = val + 3 * k
                    # Fill top-right (add 0*k)
                    grid[i][j + size] = val + 0 * k
                    # Fill bottom-left (add 2*k)
                    grid[i + size][j] = val + 2 * k
                    # Fill bottom-right (add 1*k)
                    grid[i + size][j + size] = val + 1 * k

            return grid

        return build(n)