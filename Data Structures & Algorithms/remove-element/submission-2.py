class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = 51 # constraint only has numbers from 0 to 50. 51 serves as a markor without changing types
                i += 1
            else:
                counter +=1
                i +=1
        new_list = []
        for i in nums:
            if i != 51:
                new_list.append(i)
        nums[:] = new_list
        
        return counter