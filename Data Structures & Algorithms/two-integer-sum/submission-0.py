class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        if len(nums)<2: return []
        for i in range(len(nums)):
            req=target-nums[i]
            if req in check: return [check[req],i]
            else: check[nums[i]]=i
        return []