def Counting(num):
    Num = 0
    for i in range(0, num):
        Num = Num+i

    return Num

def main():
    num = 5
    out = Counting(num)
    print(f"The total counting is {out}")


if __name__ == "__main__":
    main()