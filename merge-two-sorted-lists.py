# my original implementation
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        sortedList = dummy
        left, right = list1, list2
        while left and right:
            if left.val <= right.val:
                sortedList.next = ListNode(left.val)
                sortedList = sortedList.next
                left = left.next
            else:
                sortedList.next = ListNode(right.val)
                sortedList = sortedList.next
                right = right.next
        if right:
            sortedList.next = right
        elif left:
            sortedList.next = left
        return dummy.next

# optimized code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next  = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

# recursive solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        def sort(l1, l2, cur):
            if not l1 or not l2:
                cur.next = l1 or l2
                return
                
            if l1.val <= l2.val:
                val = l1.val
                cur.next = ListNode(val)
                sort(l1.next, l2, cur.next)
            else:
                val = l2.val
                cur.next = ListNode(val)
                sort(l1, l2.next, cur.next)

        sort(list1, list2, cur)
        return dummy.next
