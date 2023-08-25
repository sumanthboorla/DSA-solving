class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        n=n[2:]
        n=str(n).count('1')
        return n
        # l=list(map(int,n))
        # return sum(l)
        