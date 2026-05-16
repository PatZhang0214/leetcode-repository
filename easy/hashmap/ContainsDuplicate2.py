def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # nums = [1,2,3,1], k = 3
    # Output: true
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i - k])
    return False