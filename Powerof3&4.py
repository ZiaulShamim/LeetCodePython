def PowerOfThr(n):
    # Here is one way
    # if (n <= 0):
    #         return False

    # while(n>1):
    #     mod = n%3
    #     if(mod >0):
    #         return False
    #         break
        
    #     n = n//3

    # return True

# Here is another way

    if(n<=0):
         return False
    
    if(1162261467 % n == 0):
         return True
    else:
         return False 



def PowerOfFou(num):
    if (num <= 0):
            return False

    while(num>1):
        mod = num%4
        if(mod >0):
            return False
            break
        num = num//4
        
    return True


def main():
    n1 = 3
    n2 = 4
    n3 =27
    n4 = 16

    Out1 = PowerOfThr(n1)
    Out2 = PowerOfThr(n2)
    Out3 = PowerOfThr(n3)
    Out4 = PowerOfThr(n4)

    Out5 = PowerOfFou(n1)
    Out6 = PowerOfFou(n2)
    Out7 = PowerOfFou(n3)
    Out8 = PowerOfFou(n4)

    print(f"The {n1} {Out1} Power of 3")
    print(f"The {n2} {Out2} Power of 3")
    print(f"The {n3} {Out3} Power of 3")
    print(f"The {n4} {Out4} Power of 3")

    print()
    print()

    print(f"The {n1} {Out5} Power of 3")
    print(f"The {n2} {Out6} Power of 3")
    print(f"The {n3} {Out7} Power of 3")
    print(f"The {n4} {Out8} Power of 3")



if __name__ == "__main__":
    main()

