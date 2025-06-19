class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        flag=False
        for i in s:
            if i=="(" or i=="[" or i=="{":
                arr.append(i)
            else:
                if len(arr)>0:
                    m=arr.pop()
                    if (m=="(" and i==")") or (m=="[" and i=="]") or (m=="{" and i=="}"):
                        continue
                    else:
                        return False
                else:
                    return False
        return len(arr)==0