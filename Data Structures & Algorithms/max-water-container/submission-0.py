class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        res=(j-i)*min(heights[i],heights[j])
        while i<j:
            ans=(j-i)*min(heights[i],heights[j])
            res=max(ans,res)
            if heights[i]<heights[j]:
                i+=1
            else: j-=1
        return res