class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = []
        l, r = 0, 0
        while l < len(arr) and len(temp) < len(arr):
            temp.append(arr[l])
            if arr[l] == 0:
                temp.append(0)
            l +=1
        for i in range(len(arr)):
            arr[i] = temp[i]
