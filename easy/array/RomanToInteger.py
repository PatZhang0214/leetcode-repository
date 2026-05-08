def romanToInt(s: str) -> int:
    numeral_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
    'XC': 90, 'CD': 400, 'CM': 900}
    total = 0
    i = len(s) - 1
    for i in range(len(s)):
        if i < len(s) - 1 and numeral_dict[s[i]] < numeral_dict[s[i + 1]]:
            total -= numeral_dict[s[i]]
        else:
            total += numeral_dict[s[i]]
    return total

if __name__ == '__main__':
    print(romanToInt('LVIII'))