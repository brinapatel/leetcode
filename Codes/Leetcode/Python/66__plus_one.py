def plusOne(self, digits: List[int]) -> List[int]:
    num_str = "".join([str(item) for item in digits])
    new_num = int(num_str) + 1
    return [int(item) for item in str(new_num)]