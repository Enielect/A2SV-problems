class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)
        seen = set()

        mini = len(nums) // 3
        for num in nums:
            hash_map[num] +=1
            if hash_map[num] > mini:
                seen.add(num)
        return list(seen)
