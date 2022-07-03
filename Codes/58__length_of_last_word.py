def lengthOfLastWord(self, s: str) -> int: 
    rev = s[::-1].rstrip(' ').lstrip(' ')
    si = rev.split(' ')
    return len(si[0][::-1])