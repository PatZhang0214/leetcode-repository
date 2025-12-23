from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        
        i = 0
        ptr1 = 0
        
        nums[i] == 0
        nums[ptr1] = nums[i]
        
    """
    ptr1 = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[ptr1], nums[i] = nums[i], nums[ptr1]
            ptr1 += 1
if __name__ == '__main__':
    arr1 = [ 1, 2, 3]
    moveZeroes(arr1)
    print(arr1)