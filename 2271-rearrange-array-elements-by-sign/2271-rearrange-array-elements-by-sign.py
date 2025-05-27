class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        mini=min(len(pos),len(neg))
        for i in range(mini):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
        if len(pos)>len(neg):
            for i in range(mini,len(pos)):
                nums[i+mini]=pos[i]
        else:
            for i in range(mini,len(neg)):
                nums[i+mini]=neg[i]
        return nums