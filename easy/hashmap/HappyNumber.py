def isHappy(n: int) -> bool:
    st = set()
    while True:
        n = str(n)
        total = 0
        for c in n:
            total += int(c) ** 2
        n = total
        if n == 1:
            return True
        if n in st:
            return False
        print(n)
        st.add(n)

if __name__ == '__main__':
    print(isHappy(19))