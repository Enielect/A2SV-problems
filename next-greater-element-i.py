class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = defaultdict(lambda: -1)
        stack = [] # monotonic decreasing stack 
        for num in nums2:
            while stack and stack[-1] <= num:
                hash_map[stack.pop()] = num
            stack.append(num)
        
        return [hash_map[x] for x in nums1]
