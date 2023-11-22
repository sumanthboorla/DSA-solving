class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=[]
        for i in sentences:
            count.append(len(i.split(' ')))
        return max(count)
        
        
        