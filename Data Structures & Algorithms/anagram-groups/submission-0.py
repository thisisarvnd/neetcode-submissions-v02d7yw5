class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            if sort not in hashmap:
                hashmap[sort] = [i]
            else:
                hashmap[sort].append(i)
        
        output = []
        for i in hashmap.values():
            pair = []
            for j in i:
                pair.append(strs[j])
            output.append(pair)
        return output