class Solution:
    def findRightInterval(self, ivals: List[List[int]]) -> List[int]:
        n = len(ivals)
        hm = {x[0]: i for i,x in enumerate(ivals)}
        srt = sorted(ivals)
        res = []

        for s,e in ivals:
            l,r = 0, n - 1
            closest = -1
            while l <= r:
                m = (l+r)//2
                cur = srt[m]
                
                if srt[m][0] < e:
                    l = m + 1
                else:
                    closest = hm[srt[m][0]]
                    r = m - 1
            res.append(closest)
        return res
