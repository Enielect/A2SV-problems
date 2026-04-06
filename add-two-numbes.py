# initial
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l3 = dummy

        cur_sum = 0
        carry = 0
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            carry = cur_sum // 10

            l3.next = ListNode(cur_sum % 10)

            l3 = l3.next
            l2 = l2.next
            l1 = l1.next
        
        while l1:
            cur_sum = carry + l1.val
            carry = cur_sum // 10

            l3.next = ListNode(cur_sum % 10)

            l1 = l1.next
            l3 = l3.next
        
        while l2:
            cur_sum = carry + l2.val
            carry = cur_sum // 10
 
            l3.next = ListNode(cur_sum % 10)

            l2 = l2.next
            l3 = l3.next

        while carry:
            l3.next = ListNode(carry)
            carry = carry // 10
            l3 = l3.next
        return dummy.next

# what should be the optimal solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l3 = dummy

        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10

            l3.next = ListNode(total % 10)
            l3 = l3.next
        return dummy.next
