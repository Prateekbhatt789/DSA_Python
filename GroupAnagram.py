# LeetCode 49: Group Anagram
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        if len(strs)==1 and strs[0]=="":
            return [[""]]
        result = []
        anagram_map = {}
        for word in strs:
            freq_list = [0]*26
            for ch in word:
                index = ord(ch)-ord('a')
                freq_list[index] +=1
            freq_tuple = tuple(freq_list)
            if not freq_tuple in anagram_map:
                anagram_map[freq_tuple] = []
            anagram_map[freq_tuple].append(word)

        return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))