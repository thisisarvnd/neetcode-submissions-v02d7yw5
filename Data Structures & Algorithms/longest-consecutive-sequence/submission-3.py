class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        indexp1 = []
        consec = []
        for i in range(len(nums)):
            if nums[i] + 1 in nums:
                indexp1.append(i)
        for i in indexp1:
            end = False
            counter = 1
            while end == False:
                if nums[i] + counter in nums:
                    counter += 1
                else:
                    end = True
            consec.append(counter)
        return max(consec)