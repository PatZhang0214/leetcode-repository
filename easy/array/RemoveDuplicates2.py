def removeDuplicates(nums: List[int]) -> int:
    write = 0
    for num in nums:
        if write < 2 or num != nums[write - 2]:
            nums[write] = num
            write += 1
    return write
if __name__ == '__main__':
    print(removeDuplicates([1,1,1,2,2,3]))