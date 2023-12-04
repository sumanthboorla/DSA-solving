class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        mergedlist=[]
        for i in range(len(intervals)):
            if mergedlist==[]:
                mergedlist.append(intervals[i])
            else:
                prev_end = mergedlist[-1][1]
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
                if(prev_end >= curr_start):
                    mergedlist[-1][1] = max(prev_end , curr_end)
                else:
                    mergedlist.append(intervals[i])
                
        return mergedlist
                