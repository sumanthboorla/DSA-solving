class Solution:
    def sumZero(self, n: int) -> List[int]:
        L=[]
        if(n%2==0):
            n=n//2
            for i in range(-n , n+1):
                if(i==0):
                    pass
                else:
                    L.append(i)
        else:
            n=n//2
            for i in range(-n , n+1):
                    L.append(i)

        return L
        