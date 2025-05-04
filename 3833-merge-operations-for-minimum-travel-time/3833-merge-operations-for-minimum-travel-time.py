class Solution:
    def minTravelTime(self, l: int, n: int, k: int, p: List[int], t: List[int]) -> int:
        s = [0]
        for v in t:
            s.append(s[-1] + v)

        INF = 10**18
        dp = [[defaultdict(lambda: INF) for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][t[0]] = 0

        for i in range(n - 1):
            for c in range(k + 1):
                for cur, cost in dp[i][c].items():
                    for j in range(i + 1, n):
                        r = j - i - 1
                        nc = c + r
                        if nc > k:
                            break
                        dist = p[j] - p[i]
                        nxt1 = cost + dist * cur
                        nxt2 = s[j + 1] - s[i + 1]
                        d = dp[j][nc]
                        if nxt1 < d.get(nxt2, INF):
                            d[nxt2] = nxt1

        return min(dp[n - 1][k].values())