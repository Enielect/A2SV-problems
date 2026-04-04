# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # naive solution
        val = ''
        while head:
            val += str(head.val)
            head = head.next
        
        l, r = 0, len(val) - 1
        while l < r:
            if val[l] != val[r]:
                return False
            l +=1
            r -=1
        return True

# optimized solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prv = None
        while slow:
            temp = slow.next
            slow.next = prv
            prv = slow
            slow = temp
        
        first, second = head, prv
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
