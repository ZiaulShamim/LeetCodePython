def Fibonacci(num):
    nm1 = 0
    nm2 = 1

    if(num == 0):
        return 0
    else:
        for i in range(1, num+1, 1): #   # 0,1 -> 1 (1,1)->2 (1,2)->3 (2,3)-> 5
            out = nm1 + nm2  # 0, 1, 2, 3, 5, 8, 13
            nm1 = nm2
            nm2 = out

        return out

def printFibonacci():
    pass


def Tribonacci(n):
    n1 = 0
    n2 = 1
    n3 = 1

    if (n== 0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1            
    else:
        for i in range(3, n+1):
            total = n1 + n2 +n3
            n1 = n2
            n2 = n3
            n3 = total

        return total

def main():
    num = 25
    pibNum = Fibonacci(num)
    print(f"The fibonacci number of {num} is {pibNum}")

    tibNum = Tribonacci(num)

    print(f"The Tribonacci number of {num} is {tibNum}")



if __name__ == "__main__":
    main()