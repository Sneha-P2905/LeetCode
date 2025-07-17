class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        st=""
        for i in s:
            if i.isalnum():
                st+=i
        st=st.lower()
        n=len(st)
        i=0
        j=n-1
        while i<j:
            if st[i]!=st[j]:
                return False
            i+=1
            j-=1
        return True
        