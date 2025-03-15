# LeetCode 205: Isomorphic
def isIsomorphic(s: str, t: str) -> bool:
    if len(s)!= len(t):
        return False
    s_map = {}
    t_map = {}
    for key,val in zip(s,t):
        if (key in s_map and s_map[key]!= val) or (val in t_map and t_map[val]!=key):
            return False
        s_map[key] =val
        t_map[val] =key
    return True

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))