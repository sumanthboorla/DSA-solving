class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        sum1=0
        j=len(people)-1
        while(i<=j):
            if(people[i]+people[j]<=limit):
                i+=1
                j-=1
            else:
                j-=1
            sum1+=1
        return sum1
                
            