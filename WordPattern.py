# LeetCode 290- Word Pattern 
def wordPattern( pattern: str, s: str) -> bool:
    s_list = s.split()
    if len(s_list) != len(pattern):
        return False
    word_map = {}
    seen_map = {}
    for i,word in enumerate(s_list):
        if pattern[i] not in word_map:
            word_map[pattern[i]] = word
        if word not in seen_map:
            seen_map[word]=pattern[i]
        if word_map[pattern[i]] != word or seen_map[word] != pattern[i]: 
            return False
    return True

def wordPattern2( pattern: str, s: str) -> bool:
    s_list = s.split()
    if len(s_list) != len(pattern):
        return False
    pattern_map = {}
    word_map = {}
    for i,word in enumerate(s_list):
        if (pattern[i] in pattern_map and pattern_map[pattern[i]] != word) or (word in word_map and word_map[word] != pattern[i]): 
            return False
        pattern_map[pattern[i]] = word
        word_map[word]=pattern[i]
    return True

print(wordPattern2('abbc','cat dog dog cat'))