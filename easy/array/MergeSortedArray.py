def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
   Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    y = 0
    n_array = []
    while i < m and y < n:
        if nums1[i] < nums2[y]:
            n_array.append(nums1[i])
            i += 1
        else:
            n_array.append(nums2[y])
            y += 1
    if i < m:
        n_array.extend(nums1[i:m])
    if y < n:
        n_array.extend(nums2[y:n])
    nums1[:] = n_array

if __name__ == '__main__':
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)