# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# my original solution
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        dummy = ListNode(0, head)
        first_cut = dummy

        dummy2 = ListNode()
        reqList = dummy2

        while head:
            if count < left:
                first_cut = first_cut.next
            if left <= count <= right:
                reqList.next = ListNode(head.val)
                reqList = reqList.next
            if count == right:
                break
            head = head.next
            count +=1


        cur, prev = dummy2.next, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        last_cut = head.next
        first_cut.next = prev

        while first_cut:
            if not first_cut.next:
                first_cut.next = last_cut
                break
            first_cut = first_cut.next

# optimized code
  class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
            
        return dummy.next
