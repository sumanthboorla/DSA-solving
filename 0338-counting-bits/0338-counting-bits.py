class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            x=str(bin(i)[2:])
            sum1=0
            for j in x:
                sum1+=int(j)
            l.append(sum1)
        print(l)
        return l
            