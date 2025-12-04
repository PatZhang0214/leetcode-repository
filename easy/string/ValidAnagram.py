
def isAnagram(s: str, t: str) -> bool:
    characters = {}
    for c in s:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    for c in t:
        if c in characters:
            if characters[c] == 1:
                characters.pop(c)
            else:
                characters[c] -= 1
        else:
            return False
    if len(characters) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isAnagram( s = "nigga", t = "aggina"))