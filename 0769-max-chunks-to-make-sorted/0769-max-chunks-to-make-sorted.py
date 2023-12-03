class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        maxi=-1e6
        for i in range(0,len(arr)):
            maxi=max(maxi,arr[i])
            if(maxi<=i):
                chunk+=1
        return chunk
#         n=[]
#         for i in range(len(arr)-1):
#             if(arr[i]<arr[i+1]):
#                 n.append(i+1)       
#         if(len(n)==0):
#             return 1  
#         j=0
#         x=[]
#         for i in n:
#             x.append(arr[j:i])
#             j=i
        
        
#         print(x)
#         return len(x)

        
        
            
        
        
                        