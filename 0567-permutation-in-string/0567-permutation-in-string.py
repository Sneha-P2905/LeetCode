class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        print(k)
        arr=[]
        for i in range(len(s2)-k+1):
            str1=s2[i:i+k]
            arr.append(sorted(str1))
        return sorted(s1) in arr
        