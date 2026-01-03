from typing import Set


def lengthOfLongestSubstring(s: str) -> int:
    
    hashmap = set()
    longest = 0
    left_ptr = 0
    right_ptr = 0
    
    while right_ptr < len(s):
        if s[right_ptr] not in hashmap:
            hashmap[s[right_ptr]] = 1
            right_ptr += 1
            if len(hashmap) > longest:
                longest = len(hashmap)
        else:
            hashmap.pop(s[left_ptr])
            left_ptr += 1
    return longest

if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))