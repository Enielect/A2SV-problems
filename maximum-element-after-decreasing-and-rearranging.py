class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = sorted(arr)

        res[0] = 1
        for i in range(1, len(arr)):
            if abs(res[i] - res[i-1]) > 1:
                add = res[i-1] + 1
                res[i]  = add if add < res[i] else res[i-1]
        return res[-1]

# Found a better written solution
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        res = 1
        for i in range(1, len(arr)):
            if arr[i] >= res + 1:
                res +=1
        return res
