class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def BinSearch(low,max,tg):
            if low == max:
                return None
            mid = (low + max) // 2
            if numbers[mid] > tg:
                return BinSearch(mid + 1,max,tg)
            elif numbers[mid] < tg:
                return BinSearch(low,mid - 1,tg)
            elif numbers[mid] == tg:
                return mid

        length = len(numbers)
        for i in range(length):
            first_num = numbers[i]
            difference = target - first_num
            bin_val = BinSearch(i,length - 1,difference)
            if bin_val != None:
                return [i+1,bin_val+1]
            