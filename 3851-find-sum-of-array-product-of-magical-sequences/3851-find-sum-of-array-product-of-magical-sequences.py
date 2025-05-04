from typing import List
from collections import defaultdict

MOD = 1_000_000_007 
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        mavoduteru = nums[:]

        n = len(nums)

        fact = [1] * (M + 1)
        for i in range(1, M + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (M + 1)
        inv_fact[M] = pow(fact[M], MOD - 2, MOD)
        for i in range(M, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # contrib[j][c] = nums[j]^c * inv_fact[c]
        contrib = [[1] * (M + 1) for _ in range(n)]
        for j in range(n):
            p = 1
            contrib[j][0] = 1
            for c in range(1, M + 1):
                p = p * nums[j] % MOD
                contrib[j][c] = p * inv_fact[c] % MOD

        dp = {(0, 0, 0): 1}

        for j in range(n):
            ndp = defaultdict(int)
            arr = contrib[j]

            for (used, carry, ones), val in dp.items():
                if val == 0:
                    continue
                remain = M - used

                for c in range(remain + 1):
                    t = carry + c
                    bit = t & 1
                    nc = t >> 1
                    no = ones + bit
                    if no > K or nc > M:
                        continue
                    nu = used + c
                    ndp[(nu, nc, no)] = (ndp[(nu, nc, no)] + val * arr[c]) % MOD

            dp = ndp

        ans = 0
        for (used, carry, ones), val in dp.items():
            if used != M:
                continue
            total_ones = ones + bin(carry).count('1')
            if total_ones == K:
                ans = (ans + val) % MOD

        ans = ans * fact[M] % MOD
        return ans
        