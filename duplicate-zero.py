class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = 0
        while l < len(arr):
            if arr[l] == 0:
                arr.insert(l + 1, 0)
                arr.pop()
                l +=1
            l +=1
