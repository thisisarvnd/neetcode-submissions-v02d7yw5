class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute forcing just to check TLE and to get a flow 
        solution = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        pairs = sorted([nums[i],nums[j],nums[k]])
                        if pairs in solution:
                            continue
                        else:
                            solution.append(pairs)
        return solution

