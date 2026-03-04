class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: (x[0], x[1]))
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] >= x:
                if res[-1][1] < y:
                    res[-1][1] = y
            else:
                res.append([x,y])
        return res
