def isHappy(n: int) -> bool:
    while n ** 2 > 10:
        n = str(n)
        total = 0
        for c in n:
            total += int(c) ** 2
        n = total
    return n == 1

if __name__ == '__main__':
    
    # 1 is Happy
    #
    print(isHappy(4))