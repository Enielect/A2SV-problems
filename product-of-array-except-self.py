# initial poor solution

# 0(2n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_left = [1] * (n + 1)
        product_right = [1] * (n + 1)

        res = []

        for r in range(n):
            product_left[r + 1] = product_left[r] * nums[r]
            product_right[n - r - 1] = product_right[n - r] * nums[n - r - 1]
        
        for i in range(n):
            res.append(product_left[i] * product_right[i + 1])
        return res

# O(n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pm = 1
        res = [1] * n
        for r in range(len(nums)):
            res[r] *= pm
            pm *= nums[r]
        sm = 1
        for l in range(n - 1, -1, -1):
            res[l] *= sm
            sm *= nums[l]
        return res
