# Leetcode 76: Minimum Window Substring

def minWindow(s: str, t: str) -> str:
        ans = ""
        m = len(s)
        n = len(t)
        if n > m:
            return ans
        count = n
        # building freq_map
        t_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch,0) + 1
        
        i = j = 0
        while j < m:
            while count and j<m:
                ch = s[j]
                if ch in t_map:
                    t_map[ch] -= 1
                    if t_map[ch] == 0:
                        count -= 1
                j += 1
            if count == 0 and ans == "" or len(ans) >= j-i+1:
                ans = s[i:j]
            while count == 0 and i<j:
                if len(ans) >= j-i:
                    ans = s[i:j]
                ch = s[i]
                if ch in t_map:
                    t_map[ch] += 1
                    if t_map[ch] > 0:
                        count += 1
                i += 1
        return ans

print(f'\"{minWindow("ADOBECODEBANC","ABC")}\"')
print(f'\"{minWindow("A","A")}\"')
print(f'\"{minWindow("A","B")}\"')
print(f'\"{minWindow("AB","A")}\"')
print(f'\"{minWindow("AA","AA")}\"')
print(f'\"{minWindow("ABC","B")}\"')
