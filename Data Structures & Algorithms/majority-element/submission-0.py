class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        maxValue = max(hashmap.values())
        for i,j in hashmap.items():
            if j == maxValue:
                return i