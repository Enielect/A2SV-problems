class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        checker1 = Counter(s1)
        checker2 = Counter()

        l = 0
        for r in range(l1):
            checker2[s2[r]] +=1
        
        if checker2 == checker1:
            return True

        for r in range(l1, l2):
            checker2[s2[r]] +=1
            checker2[s2[l]] -=1
            l +=1

            if checker2[s2[l]] == 0:
                del checker2[s2[l]]

            if checker1 == checker2:
                return True
        return False
