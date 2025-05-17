# LeetCode 243- Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    freq_map = {}
    for ch in s:
        freq_map[ch] = freq_map.get(ch,0)+1
    for ch in t:
        if ch not in freq_map or freq_map[ch] < 1:
            return False
        freq_map[ch] -= 1
        if freq_map[ch] == 0:
            del freq_map[ch]
    return len(freq_map)==0

print(isAnagram('heart','earth'))
print(isAnagram('heart','earthy'))