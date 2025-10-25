def PalinDrome1(x):

    ## 1 We could do it by bit shifting

    ## 2 We could do it by checking the number from the first and last index are equal or not
    if (x < 0):
            return False
    else:
        match = x
    newNum = 0
    while((x /10)):
        reminder = x % 10

        newNum = newNum*10
        newNum = newNum + reminder
        x = ((x -reminder)/10)

    if (match == newNum):
        return True
    else: return False
    
    
    # increaser = 10
    # increasecounter = 0
    # while((num/increaser) > 0 ):
    #     # full = num/increaser
    #     # if(full >= 1):
    #     #     increasecounter += 1
    #     increasecounter += 1
    #     increaser *= 10

    # if (increasecounter == 1) :
    #     return True
    # elif ((increasecounter/2) == 0):
    #     for 
    # else:
    #     right = (increasecounter/2)-1

    #     # 12345

    # return pass 

    ## We can do it by using the mod and reminder 
    decreaser = 10
    increaser = 1
    reminder = 0
    while((num/increaser) > 0 ):
        reminder = num % 10
        reminder += reminder
        reminder *= increaser

        decreaser *= 10
        increaser *=10

    if(reminder == num):
        return True
    else: return False

def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            match = x
            newNum = 0
            while(x >0):
                reminder = x % 10

                newNum = newNum*10
                newNum = newNum + reminder
                x = x//10  

            if (match == newNum):
                return True
            else:
                return False


    

def main():
    isit = isPalindrome(-121)
    if isit == 1 :
        print("-121 is a PlainDrome ")
    else: print("-121 is not a PlainDrome ")

    isit1 = isPalindrome(121)
    if isit1 == 1 :
        print("121 is a PlainDrome ")
    else: print("121 is not a PlainDrome ")

    isit2 = isPalindrome(10)
    if isit2 == 1 :
        print("10 is a PlainDrome ")
    else: print("10 is not a PlainDrome ")
    
    
    
if __name__ == "__main__":
    main()