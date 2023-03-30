class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
#         count=0
#         x=bin(x)[2:]
#         print(x)
#         y=bin(y)[2:]
#         for i , j in zip(x,y):
#             if(i!=j):
#                 count+=1
#         return count
        xor = x ^ y
        
        # Calculate the number of set bits in the XOR
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        
        return distance

        
        
        