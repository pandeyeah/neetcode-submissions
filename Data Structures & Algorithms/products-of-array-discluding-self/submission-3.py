class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro,zerocount=1,0
        for i in range(len(nums)):
            if nums[i]==0: zerocount+=1
            else: pro*=nums[i]
        if zerocount>1: return [0]*len(nums)
        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if zerocount: res[i]=0 if c else pro
            else: res[i]=pro//c
        return res       