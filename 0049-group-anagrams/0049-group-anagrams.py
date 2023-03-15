class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        finalarr = []
        

        for ele in strs:
            if ''.join(sorted(ele)) not in grp:
                grp[''.join(sorted(ele))] = [ele]
            else:
                grp[''.join(sorted(ele))].extend([ele])


        for value in grp.values():
            finalarr.append(value)
        return finalarr