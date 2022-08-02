class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_list = [item for item in s]
        t_list = [item for item in t]
        s_list.sort()
        t_list.sort()
        if s_list==t_list:
            return True
        else:
            return False