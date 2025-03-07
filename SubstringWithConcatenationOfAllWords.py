# Leetcode 30 Substring with concatenation of all words
from typing import List
def findSubstring(s: str, words: List[str]) -> List[int]:
    ans = []
    word_len = len(words[0])
    num_words = len(words)
    total_cat_len = word_len * num_words
    s_len = len(s)
    original_map = {}
    #  building original_map for reference
    for word in words:
        original_map[word] = original_map.get(word,0)+1
    for start in range(word_len):
        i = start
        # print(start)
        while i < (s_len - total_cat_len + 1):
            curr_map = original_map.copy()
            count = num_words
            for j in range(i,i + total_cat_len, word_len):
                substring = s[j:j+word_len]
                if not curr_map.get(substring) or curr_map[substring] == 0:
                    break
                curr_map[substring] -= 1
                count -= 1
                if count == 0:
                    ans.append(i)
            i += word_len
    return ans
print(findSubstring("barfoofoobartheamthebarfooman",["foo","bar","the"]))
print(findSubstring("barfoofoobarthefoobarman",["foo","bar","the"]))
print(findSubstring("barfoothefoobarman",["foo","bar"]))