def isSubsequence(s: str, t: str) -> bool:
    # two pointers
    x, y = 0, 0
    while x < len(s) and y < len(t):
        if s[x] == t[y]:
            x += 1
        y += 1
    return x == len(s)

if __name__ == '__main__':
    print(isSubsequence("", "abc"))