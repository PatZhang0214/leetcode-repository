from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    s = 0
    l_ptr = 0
    minimum = float('inf')
    for r in range(len(nums)):
        s += nums[r]
        while s >= target:
            minimum = min(r - l_ptr + 1, minimum)
            s -= nums[l_ptr]
            l_ptr += 1
    return minimum if minimum != float('inf') else 0
if __name__ == '__main__':
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
