def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    new_list = list(set(nums))
    new_list.sort()
    if nums == new_list:
        return False
    else:
        return True