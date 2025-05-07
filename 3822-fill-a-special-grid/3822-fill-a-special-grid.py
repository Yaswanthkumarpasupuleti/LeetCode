
class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def f(k):
            if k == 0:
                return [[0]]
            g = f(k - 1)
            m, s = len(g), len(g) ** 2 
            top = [[v + 3 * s for v in g[i]] + g[i] for i in range(m)]
            bot = [[v + 2 * s for v in g[i]] + [v + s for v in g[i]] for i in range(m)]
            return top + bot
        return f(n)