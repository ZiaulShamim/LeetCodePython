def ValidParent(str):
    for i in range(0, len(str)):
        if ( str[i]== '('):
            if ( str[i+1] ==")" or str[len(str)- (i+1)] ==")" ):
                return True
            else :
                return False

        elif (str[i]== '{'):
            if (str[i+1] =="}" or str[len(str)- (i+1)] =="}" ):
                return True
            else :
                return False
        elif (str[i]== '['):
            if (str[i+1] =="]" or str[len(str)- (i+1)] =="]" ):
                return True
            else :
                return False
        else:
            return 


def main():
    str1 = "()"
    str2 = "()[]{}"
    str3 = "(]"
    str4 = "([])"
    str5 = "([)]"

    Vstr1 = ValidParent(str1)
    Vstr2 = ValidParent(str2)
    Vstr3 = ValidParent(str3)
    Vstr4 = ValidParent(str4)
    Vstr5 = ValidParent(str5)

    print(f"{str1} is a {Vstr1} parenthesis")
    print(f"{str2} is a {Vstr2} parenthesis")
    print(f"{str3} is a {Vstr3} parenthesis")
    print(f"{str4} is a {Vstr4} parenthesis")
    print(f"{str5} is a {Vstr5} parenthesis")

    print(f"The length of the first str is {len(str1)}")


if __name__ == "__main__":
    main()