class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = r = 0
        res = []
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l +=1
            else:
                res.append(nums2[r])
                r +=1
        if l < m:
            res.extend(nums1[l:m])
        if r < n:
            res.extend(nums2[r:n])
        for i in range(len(res)):
            nums1[i] = res[i]
