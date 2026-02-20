class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        seen, colors = {}, defaultdict(int)

        for x, y in queries:
            if x in seen:
                c = seen[x]
                colors[c] -=1
                if colors[c] == 0:
                    colors.pop(c)
            seen[x] = y
            colors[y] +=1
            res.append(len(colors))
        return res 
