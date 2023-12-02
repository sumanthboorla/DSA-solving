class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in range(len(accounts)):
            x=sum(accounts[i])
            if(x>maxi):
                maxi=x
        return maxi
                
                
        