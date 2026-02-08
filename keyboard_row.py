class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []

        for word in words:
            lower_word = word.lower()
            first_ch = lower_word[0]

            target_row = None
            for row in rows:
                if first_ch in row:
                    target_row = row
                    break

            if all(ch in target_row for ch in lower_word):
                res.append(word)
        return res
