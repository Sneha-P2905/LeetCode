class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        arr=[i for i in s if i.isalnum()]
        for i in arr:
            str+=i
        str=str.lower()
        n=len(str)
        if n==0:
            return n==0
        if n==1:
            return n==1
        i=0
        j=n-1
        flag=0
        while i<j:
            if str[i]==str[j]:
                flag=1
            else:
                flag=0
                break
            i+=1
            j-=1
        return flag==1

        