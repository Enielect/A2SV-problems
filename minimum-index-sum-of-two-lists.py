class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        word_idx = {word: i for i, word in enumerate(list1)}
        idx_common = defaultdict(list)

        MIN = float("inf")
        for i in range(len(list2)):
            word = list2[i]
            if word in word_idx:
                j = word_idx[word]
                MIN = min(MIN, i + j)
                idx_common[i + j].append(word)

        return idx_common[MIN]
