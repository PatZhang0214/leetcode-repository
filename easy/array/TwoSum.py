from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    p1 = 0
    seen = {}
    while p1 < len(nums):
        compliment = target - nums[p1]
        if compliment in seen:
            return [p1, seen[compliment]]
            break
        else:
            seen[nums[p1]] = p1
            p1 += 1

if __name__ == "__main__":
    twoSum(nums = [2,7,11,15], target = 9)