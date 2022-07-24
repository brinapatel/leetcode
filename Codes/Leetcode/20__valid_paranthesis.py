class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ']' : '[',
            ')': '(',
            '}':'{'
        }
        
        c = []
        for item in s:
            if len(c)>=1 and item in brackets.keys() and c[-1] == brackets[item]:
                c.pop()
            else:
                c.append(item)

        if c == []:
            return True
        else:
            return False