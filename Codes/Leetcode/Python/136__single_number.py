class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count_dict = {}
        for item in nums:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] = 2
        for key, value in count_dict.items():
            if value == 1:
                return key
            
            
            