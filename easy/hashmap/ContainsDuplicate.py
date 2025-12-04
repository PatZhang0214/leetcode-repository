def containsDuplicate(self, nums: List[int]) -> bool:
    num = {}
    for i in nums:
        if i in num:
            return True
        else:
            num[i] = 0
    return False