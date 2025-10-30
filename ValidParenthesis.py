def ValidParent(str):
    # Here I am using the Library like the  Hashtable 

    signs = {
        "(": ")",
        "{": "}",
        "[]": "]"
    }

    list = ()

    for char in str :
        if char in "({[":
            list.append(char) # Storing the value in the list like a stack

        else:
            if not list or list[-1] != signs.get(char, ""): # Checking first that if list is empty then return false
                return False
            list.pop()

    return len(list) == 0    # Check if the list is empty or not if empty return True not then return False

def ValidParent(str1):
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

    signs = {
        "(": ")",
        "{": "}",
        "[]": "]"
    }

    ver ="("

    output = signs.get(ver, "")
    print(f"The output for {ver} is {output}")

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