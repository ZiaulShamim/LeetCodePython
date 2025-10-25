def ClimbingStr(num):
    if (num <0):
        return
    elif num == 1:
        return 1
    elif num == 2:
        return 2

    else :
        list = [1,2]  ## We can do by using the list that will cost memory complesity O(n)
        newNum = 0
        for i in range(3, num+1, 1):
            newNum = list[i -2] + list[i-3]
            list.append(newNum)
    return newNum

def ClimbingStr1(num):   # time complexity is same for both 
    if (num <0):
        return
    elif num == 1:
        return 1
    elif num == 2:
        return 2

    else :
        num1, num2 = 1,2
        for i in range(3, num+1, 1):
            newNum = num1 + num2
            num1 = num2   ## We can update the value of previous value and cost memory complesity O(1)
            num2 = newNum
    return newNum

def main():
    num = 7
    way = ClimbingStr(num)
    print(f"The Unique way of making climbing {num} numbers is {way}")

    way1 = ClimbingStr1(num)
    print(f"The Unique way of making climbing {num} numbers is {way}")

    

    # for i in range(3, num+1, 1):
    #     newNum = list[i -2] + list[i-3]
    #     list.append(newNum)
    # print(newNum)

if __name__ == "__main__":
    main()