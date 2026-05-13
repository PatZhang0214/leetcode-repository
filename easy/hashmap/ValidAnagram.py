def isAnagram(s: str, t: str) -> bool:
    c_dict = {}
    for c in s:
        if c not in c_dict:
            c_dict[c] = 1
        else:
            c_dict[c] += 1
    for c in t:
        if c not in c_dict:
            return False
        else:
            if c_dict[c] == 1:
                c_dict.pop(c)
            else:
                c_dict[c] -= 1
    return len(c_dict) == 0

if __name__ == '__main__':
    print(isAnagram("rat", "car"))