class Solution:
    def isPalindrome(self, x: int) -> bool:
        Sum=0
        n=x
        while x>0:
            r=x%10
            x=x//10
            Sum=Sum*10+r
        return n==Sum