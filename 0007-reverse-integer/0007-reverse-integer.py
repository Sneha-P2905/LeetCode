class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            sum=0
            n=len(str(x))
            while x>0:
                r=x%10
                x//=10
                if r!=0:
                    sum=sum+(r*10**(n-1))
                n-=1
            if(sum>=(-2**31) and sum<=(2**31)-1):
                return sum
            else:
                return 0
        else:
            sum=0
            m=abs(x)
            n=len(str(m))
            while m>0:
                r=m%10
                m//=10
                if r!=0:
                    sum=sum+(r*10**(n-1))
                n-=1
            if(sum>=(-2**31) and sum<=(2**31)-1):
                return sum*-1
            else:
                return 0


