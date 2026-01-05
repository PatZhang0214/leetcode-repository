from typing import List

def subarraySum( nums: List[int], k: int) -> int:

    curr_prefix = 0
    prefixmap = {}
    count = 0
    for i in nums:
        curr_prefix = curr_prefix + i
        if curr_prefix == k:
            count += 1
        if curr_prefix - k in prefixmap:
            count += prefixmap[curr_prefix - k]
        if curr_prefix in prefixmap:
            prefixmap[curr_prefix] += 1
        else:
            prefixmap[curr_prefix] = 1
    return count

if __name__ == '__main__':
    print(subarraySum( nums = [1], k = 0))
