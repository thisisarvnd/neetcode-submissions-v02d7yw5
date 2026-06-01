class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        hashset = set(nums)
        startInt = set()
        for i in nums:
            if i+1 in hashset:
                startInt.add(i)
        consec = []
        for i in startInt:
            counter = 1
            for j in range(1,len(nums)):
                if (i + j) in hashset:
                    counter += 1
                else:
                    break
            consec.append(counter)
        return max(consec) if len(consec)!=0 else 0
