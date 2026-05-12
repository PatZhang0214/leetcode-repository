def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(start: int, end: int) -> None:
        x, y = start, end
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y -= 1

    k = k % len(nums)
    reverse(0, len(nums) - 1) # first reversal
    reverse(0, k - 1) # second reversal
    reverse(k, len(nums) - 1) # third reversal
    print(nums)

if __name__ == '__main__':
    rotate([1, 2, 3, 4, 5, 6, 7], 3)



