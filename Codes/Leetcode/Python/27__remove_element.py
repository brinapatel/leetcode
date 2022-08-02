class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # two approaches:
        while val in nums:
            nums.remove(val)
        return len(nums)

        # --------------
        
        j = 0
        for i in range(len(nums)):
            if nums[j] == val:
                nums.remove(val)
            else:
                j+=1
        return j