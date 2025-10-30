def PlusOne(arr):
    num = 0
    for i in range (0, len(arr)):
        num = (num*10) + arr[i]

    new_num = num + 1

    new_List = []
    while(new_num > 0):
        mod = new_num % 10
        new_List.insert(0, mod)  # We can use the append method as well But for that 
        new_num = (new_num - mod)//10  # we have to use the deque method to make the stack

    return new_List

def main():
    num1 = [1,2,3]
    num2 = [1,2,3,4]
    num3 = [9]

    AR1 = PlusOne(num1)
    AR2 = PlusOne(num2)
    AR3 = PlusOne(num3)
    print(AR1)
    print(AR2)
    print(AR3)


    stack = []
    stack.insert(0, 10)
    stack.insert(0, 20)
    stack.insert(0, 30)
    print(stack) 

if __name__ == "__main__":
    main()