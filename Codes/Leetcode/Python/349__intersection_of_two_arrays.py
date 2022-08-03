class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        output = []
        set_nums = set(nums2)
        for item in nums1:
            if item in set_nums and item not in output:
                output.append(item)
        return output
