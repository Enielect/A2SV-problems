class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            distance = defaultdict(int)
            for q in points:
                dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
                distance[dist] +=1
            for count in distance.values():
                res += count * (count - 1) # number of ways to select the two remaining points to make a 3-lengthed tuple
        return res
