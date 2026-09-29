class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def BinSearch(low,max,tg):
            print(low,max,tg)
            if low == max:
                return None
            mid = (low + max) // 2
            if numbers[mid] < tg:
                print("mid is small")
                return BinSearch(mid,max,tg)
            elif numbers[mid] > tg:
                print("mid is big")
                return BinSearch(low,mid - 1,tg)
            elif numbers[mid] == tg:
                return mid

        length = len(numbers)
        for i in range(length):
            first_num = numbers[i]
            difference = target - first_num
            bin_val = BinSearch(i,length - 1,difference)
            print("Bin = ",bin_val)
            if bin_val != None:
                return [i+1,bin_val+1]
            else:
                return [0,0]