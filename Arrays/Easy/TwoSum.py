class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        pairs = {}

        for i in range(len(nums)):
            complement = target-nums[i] 
            if complement in pairs:
                return [nums.index(complement),i]
            pairs[nums[i]] = complement
        return [-1,-1]