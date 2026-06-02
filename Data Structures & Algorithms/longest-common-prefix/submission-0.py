class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = len(min(strs))
        string = []
        for i in range(minLength):
            hashset = set()
            for j in strs:
                hashset.add(j[i])
            if len(hashset) > 1:
                break
            else:
                string.append(hashset.pop())
        return "".join(string)