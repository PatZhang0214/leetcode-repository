from typing import List
from typing import Set

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = set()
    for i, num in enumerate(nums):

        if num in seen:
            return True

        seen.add(num)

        if len(seen) > k:
            seen.remove(nums[i - k])
    return False

# [1, 2, 1] k = 1
'''
0, 1, seen = {}
seen = {1}, len(seen) = 1

1, 2, seen = {}
seen = {1, 2}, len{seen} = 2
seen = {2}


'''

if __name__ == '__main__':
    print(containsNearbyDuplicate(nums = [1,2,1], k = 1
))