def intToRoman1(num):
        """
        :type num: int
        :rtype: str
        """
        has = {
            1 : "I" ,
            4 : "IV",
            5 : "V" ,
            9 : "IX",
            10: "X" ,
            40: "XL",
            50: "L" ,
            90 : "XC",
            100: "C" ,
            400 : "CD",
            500: "D",
            900: "CM",
            1000: "M"
            }
        
        roman = ""
        
        while num >0:
               mod = num%10

               modToRom = has[mod]#Now cahange the mod number to roman 

               num = num - mod

def intToRoman(num):
    numbers = [1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1]
    symbols = ["M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"]

    roman = ""

    for i in range(len(numbers)):
        while num >= numbers[i]:
            roman += symbols[i]
            num -= numbers[i]

    return roman
                     
        
def main():
    num = 3749
    out = intToRoman(num)
    print(f"The roman number for {num} is {out}")

    num1 = 58
    out1 = intToRoman(num1)
    print(f"The roman number for {num1} is {out1}")

    num2 = 1994
    out2 = intToRoman(num2)
    print(f"The roman number for {num2} is {out2}")

if __name__ == "__main__":
        main()