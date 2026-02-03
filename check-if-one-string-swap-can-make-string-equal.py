class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        swap_count, pos_1, pos_2 = 0, -1, -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if pos_1 == -1:
                    pos_1 = i
                elif pos_2 == -1:
                    pos_2 = i
                swap_count  +=1

        return swap_count == 2 and s1[pos_1] == s2[pos_2] and s1[pos_2] == s2[pos_1]
