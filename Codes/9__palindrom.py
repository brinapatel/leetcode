'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

def isPalindrome(self, x: int) -> bool:
    
    num = x
    rev = 0
    while(num>0):
        rem = num%10
        rev = rev*10 + rem
        num = int(num/10)
        print(rev)
    if rev == x:
        return True
    else:
        return False