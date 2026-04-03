class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            newarr = [x for x in nums]
            del newarr[i]
            prod = 1
            for j in newarr:
                prod = prod * j
            output.append(prod)
        return output
            