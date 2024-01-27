class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            curr = [0] * (k + 1)
            total = 0  # revise sliding window

            for K in range(k + 1):
                if K >= N:
                    total -= prev[K - N]
                total = (total + prev[K]) % MOD
                curr[K] = total
            prev = curr
        return prev[K]
