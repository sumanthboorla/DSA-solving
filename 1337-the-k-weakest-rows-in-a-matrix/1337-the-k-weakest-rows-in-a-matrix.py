class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=list()
        dic=dict()
        count=0
        for i in mat:
            dic[count]=i.count(1)
            count+=1
        sorted_dict=dict(sorted(dic.items(), key=lambda item: item[1]))
        for i in sorted_dict.keys():
            if(k>0):
                k-=1
                ans.append(i)
        return ans
            
        
                
                    
        