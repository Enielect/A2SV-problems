class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # check intersections between intervals
        # check intersections between ends of one interval and the start of another interval
        l, r = 0, 0
        res = []
        while l < len(firstList) and r < len(secondList):
            start1, end1 = firstList[l]
            start2, end2 = secondList[r]
            if start1 <= end2 and start2 <= end1: # ehecking if there is an overlap (criss-crossing lock condition)
                res.append([max(start2, start1), min(end1, end2)])
            
            if end1 < end2:
                l +=1
            elif end2 < end1:
                r +=1
            else:
                l +=1
                r +=1
        return res
