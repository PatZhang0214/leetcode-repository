def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in seen:
            return [seen[compliment], i]
        seen[nums[i]] = i

print(twoSum(nums = [3,2,4], target = 6))