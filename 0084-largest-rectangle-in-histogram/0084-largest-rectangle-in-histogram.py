class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        heights.append(0)
        n=len(heights)
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                top=stack.pop()
                height=heights[top]
                width=i if not stack else i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i)
        return max_area