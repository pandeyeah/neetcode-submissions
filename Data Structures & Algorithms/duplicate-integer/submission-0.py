class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1
            
        for num in freq:
            if freq[num] >= 2: 
                return True
        return False