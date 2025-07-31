class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        max_length=float("-inf")
        max_count=float("-inf")
        count={}
        left=0
        for right in range(n):
            char=s[right]
            if char not in count:
                count[char]=0
            count[char]+=1
            max_count=max(max_count,count[char])
            if (right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
