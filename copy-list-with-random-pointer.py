"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_table = {None: None}
        temp = head

        dummy = ListNode(0)
        cur = dummy

        cp = head
        while cp:
            hash_table[cp] = Node(cp.val)
            cp = cp.next
        
        while temp:
            cur.next = hash_table[temp]
            cur.next.random = hash_table[temp.random]
            temp = temp.next
            cur = cur.next
        return dummy.next
