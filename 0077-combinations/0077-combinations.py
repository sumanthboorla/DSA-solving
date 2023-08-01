from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        L=[]
        for i in combinations(range(1,n+1),k):
            L.append(map(int,i))
        return L
            
        