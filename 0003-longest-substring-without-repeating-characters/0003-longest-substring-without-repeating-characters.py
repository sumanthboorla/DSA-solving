class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seti=set()
        start,maxlen=0,0
        for i,var in enumerate(s):
            while var in seti:
                seti.remove(s[start])
                start+=1
            seti.add(var)
            maxlen=max(maxlen,i-start+1)
        return maxlen
                
        #         char_set = set()
        # max_len, start = 0, 0
        # for i, c in enumerate(s):
        #     while c in char_set:
        #         char_set.remove(s[start])
        #         start += 1
        #     char_set.add(c)
        #     max_len = max(max_len, i - start + 1)
        # return max_len