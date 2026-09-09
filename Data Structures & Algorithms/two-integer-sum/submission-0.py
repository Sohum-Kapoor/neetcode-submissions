class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)):
            if target - nums[i] in D:
                return [D[target - nums[i]], i]
            elif nums[i] not in D:
                D[nums[i]] = i