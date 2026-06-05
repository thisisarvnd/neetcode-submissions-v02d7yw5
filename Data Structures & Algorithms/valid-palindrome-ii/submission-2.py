class Solution:
    def validPalindrome(self, s: str) -> bool:
        #absolute sphagetti of a code
        if s[::-1] == s:
            return True
        i = 0
        j = len(s) - 1
        allowed = True
        keys = []
        while i != j and not i >= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                if allowed and j!=len(s)-1:
                    allowed = False
                    keys.append(i)
                    keys.append(j)
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
        newstr = list(s)
        print(newstr,keys)
        del newstr[keys[0]]
        del newstr[keys[1]-1]
        print(newstr)
        newstr = "".join(newstr)
        if newstr == newstr[::-1]:
            return True
        else:
            return False
        