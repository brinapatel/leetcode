def majorityElement(self, nums: List[int]) -> int:
    
    d = {}
    
    for item in nums:
        if item in d:
            d[item] += 1
            if d[item]>= len(nums)/2:
                return item
        else:
            d[item] = 1
    return nums[0]

'''
#Method2

nums.sort()
return nums[len(nums)//2]
'''