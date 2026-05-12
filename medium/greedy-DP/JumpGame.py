def canJump(nums: List[int]) -> bool:
    # at each index, we need to check if it is even possible to reach that index
    # we start at 0

    '''
    [2 3 1 1 4]
    at i = 1, num = 3
    we can jump to i = 1 because 2 >= 1
    we can now jump to i = 2, 3, 4
    
    maximum of where we can jump = max[2 (from i = 0), 4 (from i = 1)] = 4

    at i = 2, num = 1
    we can jump to i = 2 because 4 >= 2
    we can now jump to i = 3
    
    maximum of where we can jump = max[3 (from i = 2), 4 (from i = 1)] = 4
    
    at i = 3, num = 1
    we can jump to i = 3 because 4 >= 3
    we can now jump to i = 4
    
    maximum of where can jump = max[4 (from i = 3), 4 (from i = 1)] = 4
    
    at i = 4, we can jump because 4 >= 4
    
    ____________________________________________________________________________________
    
    nums = [3 2 1 0 4]
    
    at i = 1, num = 2
    we can jump to i = 1 because 3 >= 1
    we can now jump to i = 2, 3
    
    maximum of where we can jump = max[3 (from i = 0), 2 (from i = 1)] = 3
    
    at i = 2, num = 1
    we can jump to i = 2 because 3 >= 2
    we can now jump to i = 3
    
    maximum of where we can jump = max[3 (from i = 0), 1 (from i = 2)] = 3

    at i = 3, num = 0
    we can jump to i = 3 because 3 >= 3
    we cannot jump anywhere

    maximum of where we can jump = max[3 (from i = 0), 1 (from i = 2)] = 3

    since max now equals i = 3 AND NOT len(nums) - 1 => False

    '''
    max_jump = nums[0]
    for i in range(len(nums)):
        jump = nums[i]
        jump = i + jump
        max_jump = max(jump, max_jump)

        if max_jump <= i and i != len(nums) - 1:
            return False
    return True


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4]))