class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        sum1=0
        n=abs(x)
        while n>0:
            r=n%10
            n=n//10
            sum1=sum1*10+r
        result=sum1*sign
        if  result>=(-2)**31 and result<=(2)**31-1:
            return result
        else:
            return 0