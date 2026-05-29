class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def BinSearch(low,high,tg):
            print("binary")
            if low == high:
                return -1
            mid = (low + high) // 2
            if numbers[mid] == tg:
                return mid
            elif numbers[mid] > tg:
                return BinSearch(low,mid,tg)
            elif numbers[mid] < tg:
                return BinSearch(mid,high,tg)
        
        for i in range(0,len(numbers)):
            tg = target - numbers[i]
            value = BinSearch(i+1,len(numbers),tg)
            if value > 0:
                return [i+1, value+1]