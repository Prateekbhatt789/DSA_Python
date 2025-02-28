import typing
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    charSet = set()
    i =0
    wlen =0
    for j in range(n):
        while s[j] in charSet:
            charSet.remove(s[i])
            i+=1
        charSet.add(s[j])
        wlen = max(wlen, j-i+1)
        
    return wlen

print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))