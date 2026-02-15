class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # go through all the ghosts and check wheterh the number of steps
        # it takes the ghost to get to the origin is larger than mine

        endx, endy = target
        my_steps = abs(endx) + abs(endy)
        
        for x, y in ghosts:
            steps = abs(x - endx) + abs(y - endy)
            if steps <= my_steps:
                return False
        return True
