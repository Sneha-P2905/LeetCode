class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        else:
            open_count=0
            res=0
            for i in s:
                if i=="(":
                    open_count+=1
                else:
                    open_count-=1
                    if open_count<0:
                        open_count=0
                        res+=1
            return res+open_count