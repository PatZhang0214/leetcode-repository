def strStr(haystack: str, needle: str) -> int:
    if needle == haystack:
        return 0
    # two pointers
    # i is first pointer (beginning)
    # y is the ending pointer (end)
    i = 0
    y = len(needle)
    while y <= len(haystack):
        print(haystack[i:y])
        if needle != haystack[i:y]:
            i += 1
            y += 1
        else:
            return i
    return -1

if __name__ == '__main__':
    print(strStr("hello", "lo"))


