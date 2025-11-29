def StringToNum(str):
    int_max = 2**31 - 1
    int_min = - 2 **31


    i  = 0 
    n = len(str)
    while i < n and str[i] == " ":
        i += 1

    if i == n :
        return 0
    
    sign = 1 
    if str[i] == "-":
        sign = -1
        i += 1
    if str[i] == "+":
        sign = 1
        i += 1

    num = 0 
    while i < n and str[i].isdigit():   # as the first non-digit string value it will stop even it is not 1 
        digit = ord(str[i]) - ord("0") # convert char to in t by negate the Asci of of the zero form the character 

        if num > (int_max - digit)// 10:
            return int_max if sign == 1 else int_min
        
        num = num * 10 + digit
        i += 1


    return sign*num



def main():
    s = "42"
    out = StringToNum(s)
    print(f"The number of the string {s} is {out}")

    s1 = " -042"
    out1 = StringToNum(s1)
    print(f"The number of the string {s1} is {out1}")

    s2 = "1337c0d3"
    out2 = StringToNum(s2)
    print(f"The number of the string {s2} is {out2}")

    s3 = "0-1"
    out3 = StringToNum(s3)
    print(f"The number of the string {s3} is {out3}")

    s4 = "words and 987"
    out4 = StringToNum(s4)
    print(f"The number of the string {s4} is {out4}")


if __name__ == "__main__":
    main()