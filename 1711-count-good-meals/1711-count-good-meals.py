# from itertools import combinations
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
#         l=[]
#         for i in combinations(deliciousness,2):
#             l.append(list(i))
#         print(l)
#         sum2=[]
#         for i in l:
#             sum1=0
#             for j in i:
#                 sum1+=j
#             sum2.append(sum1)

#         print(sum2)
#         sum3=[]
#         for x in sum2:
#             if(x and (not(x & (x - 1)))):
#                 sum3.append(x)
#         return len(sum3)
        from collections import defaultdict
        dp = defaultdict(int)
        # ds.sort() # no need to sort
        res = 0
        
        for d in deliciousness:
            for i in range(22):
                # if 2**i - d in dp:
                res += dp[2**i - d]
            dp[d] += 1
        return res % (10**9 + 7)