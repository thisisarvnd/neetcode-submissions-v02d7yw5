class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        length = len(nums) -1
        print(nums)
        for i in range(length):
            target = 0 - nums[i]
            j = i+1
            k = length
            while j<k:
                comp = nums[j] + nums[k]
                if comp == target:
                    temp = [nums[i],nums[j],nums[k]]
                    if temp in solution:
                        continue
                    else:
                        solution.append(temp)
                elif comp > target:
                    k -= 1
                elif comp < target:
                    j += 1
        return solution

