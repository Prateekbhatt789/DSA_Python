#  Leetcode 125: Valid Palindrome
import string

def isPalindrome(s: str) -> bool:
    s = ''.join([char for char in s if char.isalnum()])
    s = s.lower()
    i,j = 0 , len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

# Best code
def isPalindrome2(s:str) -> bool:
    translator = str.maketrans('','',string.punctuation+ ' _')
    print("translator:",translator)
    cs= s.translate(translator)
    print("cs:",cs)
    x = cs[::-1]
    if x.lower() == cs.lower():
        return True
    else: 
        return False

print(isPalindrome("rac a car"))
print(isPalindrome2("rac a car"))
