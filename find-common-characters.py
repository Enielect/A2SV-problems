class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash_map, res = {}, []

        for i in range(len(words)):
            word = words[i]
            hash_map[i] = Counter(word)

        a = ord('a')
        for asc in range(a, a + 27):
            ch = chr(asc)
            min_count = float("inf")

            for key in hash_map:
                min_count = min(min_count, hash_map[key][ch])
            if min_count > 0:
                res.extend([ch]*min_count)
        
        return res
