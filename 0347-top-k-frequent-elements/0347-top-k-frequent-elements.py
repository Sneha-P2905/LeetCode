class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        result=list(d.items())
        result.sort(key=lambda x:x[1],reverse=True)
        arr=[]
        for i in range(k):
            arr.append(result[i][0])
        return arr