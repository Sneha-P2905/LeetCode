class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            sum=0
            n=len(str(x))
            m=x
            while m>0:
                r=m%10
                m//=10
                if r!=0:
                    sum+=(r*10**(n-1))
                n-=1
            return sum==x
        elif x==0:
            return x==0
        else:
            sum=0
            n=len(str(abs(x)))
            m=abs(x)
            while m>0:
                r=m%10
                m//=10
                if r!=0:
                    sum+=(r*10**(n-1))
                n-=1
            str1=str(sum)+"-"
            return str1==str(x)
            

        