MOD = 10**9 + 7
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        n = len(nums)

        fact = [1] * (M+1)
        inv_fact = [1] * (M+1)
        for i in range(1, M+1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[M] = pow(fact[M], MOD-2, MOD)
        for i in reversed(range(M)):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

        pre = [[1]*(M+1) for _ in range(n)]
        for i in range(n):
            for c in range(1, M+1):
                pre[i][c] = pre[i][c-1] * nums[i] % MOD
                pre[i][c] = pre[i][c] * inv_fact[1] % MOD 
                
            for c in range(M+1):
                pre[i][c] = pow(nums[i], c, MOD) * inv_fact[c] % MOD

        dp = [{} for _ in range(n+1)]
        dp[0][(0, 0, 0)] = 1

        for i in range(n):
            for (used, carry, ones) in dp[i]:
                curr_val = dp[i][(used, carry, ones)]
                remaining = M - used
                for c in range(remaining + 1):
                    new_used = used + c
                    s = carry + c
                    bit = s & 1
                    new_carry = s >> 1
                    new_ones = ones + (1 if bit == 1 else 0)
                    if new_ones > K:
                        continue
                    factor = pre[i][c]
                    new_val = curr_val * factor % MOD
                    key = (new_used, new_carry, new_ones)
                    dp[i+1][key] = (dp[i+1].get(key, 0) + new_val) % MOD

        ans = 0
        for (used, carry, ones) in dp[n]:
            if used != M:
                continue
            extra = bin(carry).count("1")
            total_ones = ones + extra
            if total_ones == K:
                ans = (ans + dp[n][(used, carry, ones)]) % MOD
        ans = ans * fact[M] % MOD
        return ans
        