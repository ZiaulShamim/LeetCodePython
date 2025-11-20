def ReverseInt(num):
    rev = 0
    sign = -1 if num < 0 else 1
    num = abs(num)

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return sign * rev



def main():
    x = 123
    out = ReverseInt(x)
    print(f"The reverse of {x} is {out}")

    x1 = -123
    out1 = ReverseInt(x1)
    print(f"The reverse of {x1} is {out1}")

    x2 = 120
    out2 = ReverseInt(x2)
    print(f"The reverse of {x2} is {out2}")

if __name__ == "__main__":
    main()