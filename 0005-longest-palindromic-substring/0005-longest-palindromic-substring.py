class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        else:
            l = []
            for i in range(len(s)+1):
                for j in range(i):
                    a = (s[j:i])
                    if a==a[::-1]:
                        l.append(a)
            
            l.sort(key=len)
            return l[-1]
        