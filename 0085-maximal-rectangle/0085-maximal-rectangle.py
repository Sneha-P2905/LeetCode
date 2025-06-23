class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n=len(matrix[0])
        height=[0]*n
        max_area=0
        for row in matrix:
            for i in range(n):
                if row[i]=='1':
                    height[i]+=1
                else:
                    height[i]=0
            max_area=max(max_area,self.largestRectangleArea(height))
        return max_area
    def largestRectangleArea(self,height):
        max_area=0
        stack=[]
        height.append(0)
        n=len(height)
        for i in range(n):
            while stack and height[stack[-1]]>height[i]:
                top=stack.pop()
                h=height[top]
                w=i if not stack else i-stack[-1]-1
                max_area=max(max_area,h*w)
            stack.append(i)
        height.pop()
        return max_area