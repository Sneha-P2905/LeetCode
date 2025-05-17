class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        arr=[i for i in s if i.isalnum()]
        for i in arr:
            str+=i
        str=str.lower()
        return str==str[::-1]

        