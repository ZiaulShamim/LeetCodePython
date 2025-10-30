def TwoPower(num):
    while(num >2):
        mod = num % 3
        if(mod >0):
            return False
            break
        num = num // 3
    return True

def main():
    n1 = 9
    n2 = 16
    n3 = 3

    Out1 = TwoPower(n1)
    Out2 = TwoPower(n2)
    Out3 = TwoPower(n3)

    print(f"The {n1} is {Out1} is a power of 2")
    print(f"The {n2} is {Out2} is a power of 2")
    print(f"The {n3} is {Out3} is a power of 2")

    print("this is the code !")
    print(-16//2)
    print(-16%2)

if __name__ == "__main__":
    main()