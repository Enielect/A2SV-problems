class Solution:    
    def findUnion(self, a, b):
        # code here
        return set(a) | set(b)

    def findUnion1(self, a, b):
        # code here
        seen = set(a)
        
        for num in b:
            seen.add(num)
        return seen
