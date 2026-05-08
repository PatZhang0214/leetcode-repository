def longestCommonPrefix(strs: List[str]) -> str:
    pref = ""
    z = 0
    i = 0
    minlength = len(strs[0])
    for s in strs:
        if len(s) < minlength:
            minlength = len(s)

    while i < minlength:
        curr = s[i]
        for s in strs:
            if s[i] != curr:
                return pref
        pref += curr
        i += 1
    return pref

if __name__ == '__main__':
    print(longestCommonPrefix(strs  = ["fl","flower","flight"]))