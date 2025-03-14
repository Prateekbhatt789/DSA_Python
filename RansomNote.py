# LeetCode 383- Ransom NoteNote
def canConstruct(ransomNote: str, magazine: str) -> bool:
    word_map = {}
    for ch in magazine:
        word_map[ch] = word_map.get(ch,0) + 1
    for ch in ransomNote:
        if ch not in word_map or word_map[ch] < 1:
            return False
        word_map[ch] -= 1
    return True

print(canConstruct('a','b'))
print(canConstruct('aa','aab'))