class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = int(len(nums))
        while(start<end):
            mid = (start+(end-start)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid
            else:
                start = mid+1
        return -1