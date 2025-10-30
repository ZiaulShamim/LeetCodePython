def Numof1Bits(num):
    if (num == 0):
        return "0"
    
    bits = []

    while(num):
        bits.append(str(num & 1))
        num >>= 1

    return ''.join(reversed(bits))

    # counter = 0

    # for i in range(0,len(bits)):
    #     if(bits[i] == '1'):
    #         counter = counter +1

    # return counter


def main():
    num = 3
    num2 = 128
    num3 = 2147483645

    Out1 = Numof1Bits(num)
    Out2 = Numof1Bits(num2)
    Out3 = Numof1Bits(num3)

    print(f"1's of {num} is {Out1}")
    print(f"1's of {num2} is {Out2}")
    print(f"1's of {num3} is {Out3}")

if __name__ == "__main__":
    main()