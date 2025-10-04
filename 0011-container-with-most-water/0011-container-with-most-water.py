class Solution:
    def maxArea(self, height: List[int]) -> int:
        water=-1
        left=0
        right=len(height)-1
        while left<right:
            area=(right-left)*min(height[left],height[right])
            water=max(water,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water
            
        