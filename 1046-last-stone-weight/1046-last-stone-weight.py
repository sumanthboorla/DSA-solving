class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones)>1):
            max1=stones.pop(-1)
            max2=stones.pop(-1)
            if(max1!=max2 ):
                stones.append(abs(max1-max2))
            stones.sort()
            
        if(len(stones)>=1):
            return stones[0]
        else:
            return 0
            
            