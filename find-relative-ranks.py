class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score)
        finish = {}
        count = 0
        positions = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while len(finish) < len(score):
            cur = sorted_score.pop()
            if count < 3:
                finish[cur] = positions[count]
                count +=1
            else:
                finish[cur] = str(count + 1)
                count +=1
        return [finish[x] for x in score]
