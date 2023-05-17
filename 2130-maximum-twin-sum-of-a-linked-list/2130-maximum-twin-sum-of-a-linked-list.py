# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        temp=head
        while(temp):
            l.append(temp.val)
            temp=temp.next
        i=0
        j=len(l)-1
        maxi=0
        sum1=0
        while(i<j):
            if(i+j%2!=0):
                sum1=l[i]+l[j]
            else:
                sum1=l[i]+l[j]
            maxi=max(sum1,maxi)
            i+=1
            j-=1
        return maxi
                