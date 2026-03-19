class Solution:
    def frequencySort(self, s: str) -> str:
        frq = sorted(Counter(s).items(), key=lambda item: -item[1])
        res = []
        for f in frq:
            res.append(f[0] * f[1])
        return ''.join(res)
