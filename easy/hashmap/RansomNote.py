def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine): return False
    letters = {}
    for i in range(len(magazine)):
        if magazine[i] not in letters:
            letters[magazine[i]] = 1
        else:
            letters[magazine[i]] += 1
    
    for i in range(len(ransomNote)):
        if ransomNote[i] not in letters:
            return False
        if ransomNote[i] in letters:
            if letters[ransomNote[i]] == 0: return False
            letters[ransomNote[i]] -= 1
    return True

if __name__ == '__main__':
    print(canConstruct(ransomNote = "nigga", magazine = "aggi"))
