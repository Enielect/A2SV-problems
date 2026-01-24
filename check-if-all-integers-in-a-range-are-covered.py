class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # recommended time complexity O(m + n*z)
        seen = set()
        for start, end in ranges:
            for x in range(start, end + 1):
                seen.add(x)

        for x in range(left, right + 1):
            if not x in seen:
                return False
        return True

    # my initial approach (this has a bad time coplexity O(m*n*z)
    def isCovered1(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left, right + 1):
            inRange = False
            for start,end in ranges:
                if i in range(start, end + 1):
                    inRange = True
            if not inRange: return False
        return True
