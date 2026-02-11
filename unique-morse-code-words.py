class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformed = set()
        for word in words:
            morse = ''
            for ch in word:
                morse += transformation[ord(ch) - ord('a')]
            transformed.add(morse)
        return len(transformed)
