class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_area=float("-inf")
        while i<j:
            if height[i]<height[j]:
                mini=height[i]
            else:
                mini=height[j]
            area=mini*(j-i)
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area