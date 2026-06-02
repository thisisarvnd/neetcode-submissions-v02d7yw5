class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                del nums[i]
                length = len(nums)
            else:
                counter +=1
                i +=1
        return counter