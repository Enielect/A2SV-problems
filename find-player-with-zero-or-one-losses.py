class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # create a hash_map of players: losses
        pl_losses = {}
        res = [[], []]
        for match in matches:
            w, l = match
            pl_losses[w] = pl_losses.get(w, 0)
            pl_losses[l] = pl_losses.get(l, 0) - 1

        for pl in pl_losses:
            if pl_losses[pl] == 0:
                res[0].append(pl)
            if pl_losses[pl] == -1:
                res[1].append(pl)
        return [sorted(res[0]), sorted(res[1])]
