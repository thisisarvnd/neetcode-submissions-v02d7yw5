class Solution:
    def validPalindrome(self, s: str) -> bool:
        startptr = 0
        endptr = len(s) - 1
        while startptr <= endptr:
            if s[startptr] == s[endptr]:
                startptr += 1
                endptr -= 1
                continue
            else:
                temp_s = startptr
                temp_e = endptr
                startptr += 1
                while startptr <= endptr:
                    if s[startptr] == s[endptr]:
                        startptr += 1
                        endptr -= 1
                        continue
                    else:
                        break
                else:
                    return True
                
                startptr = temp_s
                endptr = temp_e -1
                while startptr <= endptr:
                    if s[startptr] == s[endptr]:
                        startptr += 1
                        endptr -= 1
                        continue
                    else:
                        return False
        return True
