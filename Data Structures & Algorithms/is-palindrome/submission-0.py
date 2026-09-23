class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        for c in s:
            if c.isalnum():
                newStr+=c.upper() ##we can use .lower() as well
        return newStr==newStr[::-1]
        