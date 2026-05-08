# def isPalindrome(s: str) -> bool:
#     isP = True
#     # pointer 1, pointer 2
#     x, y = 0, len(s) - 1
#     while isP and x < y:
#         while (not s[x].isalnum() or not s[y].isalnum()) and x < y:
#             if not s[x].isalnum():
#                 x += 1
#             else:
#                 y -= 1
#         if s[x].lower() != s[y].lower():
#             isP = False
#         print(s[x], s[y])
#         x += 1
#         y -= 1
#     return isP
def remove(s: str) -> str:
    new_s = ""
    for i in s:
        if i.isalnum():
            new_s += i
    return new_s

def isPalindrome(s: str) -> bool:
    s = remove(s)
    # two pointers
    x, y = 0, len(s) - 1
    isP = True
    while isP and x < y:
        if s[x].lower() != s[y].lower():
            isP = False
        x += 1
        y -= 1
    return isP

if __name__ == '__main__':
    print(isPalindrome(" "))