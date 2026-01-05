from typing import List
from typing import Set

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = set()
    length = len(nums)
    if length == 1: return False

    # first populate the set with the first k elements
    for i in range(1, min(length, k)):
        seen.add(nums[i])
    # check
    for i in range(length):
        if nums[i] in seen:
            print(nums[i])
            return True
        if i + 1 < length:
            seen.remove(nums[i + 1])
        if i + k < length:
            seen.add(nums[i + k])
    return False

if __name__ == '__main__':
    print(containsNearbyDuplicate(nums = [1,2,1], k = 1
))