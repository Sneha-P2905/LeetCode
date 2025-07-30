class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        seen=set()
        count={}
        max_count=float("-inf")
        max_length=float("-inf")
        left=0
        for right in range(len(s)):
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