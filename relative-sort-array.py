class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # implement counter and check for missing elements
        frq, missing = defaultdict(int), []
        res = []
        for a in arr1:
            if a not in arr2:
                missing.append(a)
            frq[a] +=1
        
        for a in arr2:
            if a in frq:
                res.extend([a]*frq[a]) 
        res.extend(sorted(missing))
        return res
