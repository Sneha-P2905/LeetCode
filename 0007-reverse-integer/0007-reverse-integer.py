class Solution:
    def reverse(self, x: int) -> int:
        Sum=0
        if x>0:
            while x>0:
                r=x%10
                x=x//10
                Sum=Sum*10+r
            if Sum>=(-2**31) and Sum<=2**31:
                return Sum
            else:
                return 0
        else:
            n=abs(x)
            while n>0:
                r=n%10
                n=n//10
                Sum=Sum*10+r
            if Sum>=(-2**31) and Sum<=2**31:
                return Sum*-1
            else:
                return 0

        