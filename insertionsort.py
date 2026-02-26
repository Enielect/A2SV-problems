class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            cur_min = (arr[i], i)
            for j in range(i + 1, len(arr)):
                if arr[j] < cur_min[0]:
                    cur_min = (arr[j], j)
            val, idx = cur_min
            arr[i], arr[idx] = val, arr[i]
        return arr
