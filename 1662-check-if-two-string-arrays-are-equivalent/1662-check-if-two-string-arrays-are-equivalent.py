class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=''.join(word1)
        s1=''.join(word2)
        if(s==s1):
            return True
        else:
            return False
        
        
        