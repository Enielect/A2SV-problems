class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # flip
        res = []
        def get_max_idx(limit):
            max_, idx = 0, 0
            for key, val in enumerate(arr):
                if key == limit:
                    break
                if val > max_:
                    idx = key
                    max_ = val
            return idx
        def flip(k):
            left = 0
            while left < k:
                arr[left], arr[k] = arr[k], arr[left]
                left +=1
                k -=1

        for i in range(len(arr) - 1, -1, -1):
            max_idx = get_max_idx(i + 1)
            if max_idx != i:
                if max_idx != 0:
                    flip(max_idx)
                    res.append(max_idx + 1)
                flip(i)
                res.append(i + 1)
        return res
