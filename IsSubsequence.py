# Leetcode 392: Is Subsequence
def isSubsequence(s: str, t: str) -> bool:
    i=0
    j=0
    a= len(s)
    b= len(t)
    if a>b:
        return False
    while j<b:
        if i<a and s[i]==t[j]:
            i+=1
        j+=1

    return True if i==a else False


# Best code
def isSubsequence2(s: str, t: str) -> bool:
        a=len(s)
        b=len(t)

        if s=='':return True
        if a>b:return False
        i=0
        for j in range(b):
            if t[j]==s[i]:
                if i==a-1:
                    return True
                else:
                    i=i+1
        return False

print(isSubsequence('abc','ahbgdc'))
print(isSubsequence2('abc','ahbgdc'))