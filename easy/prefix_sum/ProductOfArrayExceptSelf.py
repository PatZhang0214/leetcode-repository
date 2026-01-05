from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    
    
    '''
    nums = [1, 2, 3, 4]
    
    prefix = [1, 2, 6, 24]
           = [1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4]
    suffix = [24, 24, 12, 4]
           = [1 * 2 * 3 * 4, 2 * 3 * 4, 3 * 4, 4]
    
    at i = 0:
    productExceptSelf[0] = 2 * 3 * 4 = 24 = suffix[1]
    productExceptSelf[1] = 1 * 3 * 4 = 12 = prefix[0] * suffix[2]
    productExceptSelf[2] = 1 * 2 * 4 = 8 = prefix[1] * suffix[3]
    productExceptSelf[3] = 1 * 2 * 3 = 6 = prefix[2]
    
    nums = [-1,1,0,-3,3]
    prefix = [-1, -1, 0, 0, 0]
           = [-1, -1 * 1, -1  * 1 * 0, -1 * 1 * 0 * -3, -1 * 1 * 0 * -3 * 3]
    suffix = [0,0,0,-9,3]
           = [-1 * 1 * 0 * -3 * 3, 1 * 0 * -3 * 3, 0 * -3 * 3, -3 * 3, 3]
    productExceptSelf[0] = 1 * 0 * -3 * 3 = suffix[1]
    productExceptSelf[1] = -1 * 0 * -3 * 3 = prefix[0] * suffix[2]
    productExceptSelf[2] = -1 * 1 * -3 * 3 = prefix[1] * suffix[3]
    productExceptSelf[3] = -1 * 1 * 0 * 3 = prefix[2] * suffix[4]
    productExceptSelf[4] = -1 * 1 * 0 * -3 = prefix[3]
    '''
    prefix = []
    pproduct = 1
    sproduct = 1
    suffix = []
    answer = []
    for i in range(len(nums)):
       pproduct *= nums[i]
       prefix.append(pproduct)
       sproduct *= nums[len(nums) - 1 - i]
       suffix.insert(0, sproduct)

    for i in range(len(nums)):
       if i == 0:
              print("suffix[1]: ", suffix[1])
              answer.append(suffix[1])
       elif i == len(nums) - 1:
              print("prefix[len(prefix) - 1]: ")
              answer.append(prefix[i - 1])
       else:
              print("prefix[i - 1] * suffix[i + 1]", i - 1, i + 1)
              answer.append(prefix[i - 1] * suffix[i + 1])

    return answer

if __name__ == '__main__':
       print(productExceptSelf([1, 2, 3, 4]))