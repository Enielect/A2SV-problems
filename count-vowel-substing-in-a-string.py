class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        hm = defaultdict(int)
        vowels = 'aeiou'
        count = 0
        for i in range(len(word)):
            if word[i] in vowels:
                for j in range(i, len(word)):
                    if word[j] in vowels:
                        hm[word[j]] +=1
                    else: 
                        break
                    if len(hm) == 5:
                        count +=1
                hm.clear()
        return count
