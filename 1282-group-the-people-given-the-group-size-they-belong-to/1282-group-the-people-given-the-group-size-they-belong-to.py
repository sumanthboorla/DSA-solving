from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dc = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dc:
                dc[groupSizes[i]] = [i]
            else:
                dc[groupSizes[i]].append(i)
                
        
        ans = []
        for key, value in dc.items():
            temp = []
            start = 0
            end = key
            while end <= len(value):
                temp = value[start:end]
                start = end
                end += key
                ans.append(temp)
        return ans