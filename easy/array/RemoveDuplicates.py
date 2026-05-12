def removeDuplicates(nums: List[int]) -> int:
    '''
    [0,0,1,1,1,2,2,3,3,4]
     x
     y
    [0,0,1,1,1,2,2,3,3,4]
     x y
    [0,0,1,1,1,2,2,3,3,4]
       x y
    [0,1,1,1,1,2,2,3,3,4]
       x y
    [0,1,1,1,1,2,2,3,3,4]
         x y
    [0,1,1,1,1,2,2,3,3,4]
         x   y
    [0,1,1,1,1,2,2,3,3,4]
         x     y
    [0,1,2,1,1,2,2,3,3,4]
         x     y
    '''
    x, y = 0, 0
    while y < len(nums):
        if nums[x] != nums[y]:
            x += 1
            nums[x] = nums[y]
        y += 1
    print(nums)
    return x + 1

if __name__ == '__main__':
    print(removeDuplicates([1, 2, 3, 4, 5]))