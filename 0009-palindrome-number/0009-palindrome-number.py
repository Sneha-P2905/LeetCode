class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        sum1=0
        n=x
        while x>0:
            r=x%10
            x=x//10
            sum1=sum1*10+r
        print(sum1)
        return n==sum1