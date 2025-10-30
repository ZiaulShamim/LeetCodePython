def BinaryStr(num1, num2):

    decNum1 = 0
    decNum2 = 0

    for i in range(0,len(num1)):
        power = len(num1) - 1 - i
        decNum1 = decNum1 + ((2**power)*int(num1[i])) 

   
    for j in range(0,len(num2)):  # a ,b= "1010", "1011"
        power = len(num2) - 1 - j  # you have to comming backword as array start from 0 and binary number start from end
        decNum2 = decNum2 + ((2**power)*int(num2[j]))
        
    # We can also use the built in method for bin to int-  int(num1, 2) + int(num2, 2)
    totalNum = decNum1 + decNum2

    if (totalNum == 0):
        return "0"
    rstr = ""
    while(totalNum >0):
        mod = totalNum % 2
        rstr = str(mod) + rstr 
        totalNum = totalNum // 2

    return (rstr)



def main():
    in1 = "11"
    in2 = "1"
    Out = BinaryStr(in1, in2)

    a = "1010"
    b = "1011"
    Out1 =BinaryStr(a,b) 

    print(Out)
    print(Out1)
    print("this is my code")

if __name__ == "__main__":
    main()