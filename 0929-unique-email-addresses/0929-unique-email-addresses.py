class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count=0
        p=set()
        for i in emails:
            x,y=i.split('@')
            empty=''
            for  j in x:
                if(j=='.'):
                    pass
                elif(j=='+'):
                    break
                else:
                    # empty=''.join(j)
                      empty+=j
            empty+='@'+y
            p.add(empty)
            print(empty)
        return len((p))
                    
                    
        