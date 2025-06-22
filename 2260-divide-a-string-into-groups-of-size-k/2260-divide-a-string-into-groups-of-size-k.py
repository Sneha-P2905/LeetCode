class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        arr=[]
        for i in range(0,n,k):
            a=s[i:i+k]
            while len(a)!=k:
                a=a+fill
            arr.append(a)
        return arr