class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverseString = "".join(t for t in s if t.isalnum()).lower()[::-1]
        #print(reverseString)
        alnumString = "".join(t for t in s if t.isalnum()).lower()
        #print(alnumString)
        if alnumString == reverseString:
            return True
        else:
            return False