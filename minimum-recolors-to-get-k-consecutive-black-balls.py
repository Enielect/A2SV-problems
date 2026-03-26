class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        changes, res = 0, 100
        l = 0

        for r in range(k):
            if blocks[r] == 'W':
                changes +=1
        res = min(res, changes)
                
        for r in range(k, len(blocks)):
            if blocks[r] == 'W':
                changes +=1
            if blocks[l] == "W":
                changes -=1
            l +=1
            res = min(res, changes)
        return res
