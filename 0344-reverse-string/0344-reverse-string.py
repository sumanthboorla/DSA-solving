class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a=len(s)//2
        b=len(s)-1
        for i in range(0,a):
            s[i],s[b]=s[b],s[i]
            b-=1
        return s
        