class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        a = 0
        b = 0
        newstr = []
        while a<i and b < j:
            print(a,b)
            newstr.append(word1[a] + word2[b])
            a += 1
            b += 1
        if a < i - 1:
            newstr.append(word1[a:i])
        elif b < j -1:
            newstr.append(word2[b:j])
        
        return "".join(newstr)