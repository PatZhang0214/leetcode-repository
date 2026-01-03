from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    curr_sum = 0
    length = len(nums)

    for i in range(k):
        curr_sum += nums[i]
    
    max_avg = curr_sum / k

    for i in range(k, length):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        max_avg = max(max_avg, (curr_sum / k))

    return max_avg

if __name__ == '__main__':
    print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    