class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        m = {}
        for i in stones:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        ans = 0
        for j in jewels:
            if j in m:
                ans += m[j]
        return ans
        