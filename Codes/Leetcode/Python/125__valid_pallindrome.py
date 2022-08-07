class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = "".join([x for x in s if x.isalnum()])

        if new_str.lower() == new_str.lower()[::-1]:
            return True
        else:
            return False