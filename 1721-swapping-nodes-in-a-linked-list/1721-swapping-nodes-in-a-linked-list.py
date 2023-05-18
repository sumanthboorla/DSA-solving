# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_beg, k_end, temp = head, head, head
        for i in range(k-1):
            temp = temp.next
        k_beg = temp
        while temp.next:
            k_end = k_end.next
            temp = temp.next
        k_beg.val, k_end.val = k_end.val, k_beg.val
        return head
        