class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        allowed = True
        while i != j and not i >= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                if allowed:
                    allowed = False
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
        return True