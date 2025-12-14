# Target : Find the position of a vlaue from an array 
def BinarySearch(arr, target):
    low = 0
    high = len(arr)- 1

    while(low <= high):
        middle = (low + high )//2   
        # middle = low +  (high - low)//2   # low might change after get rid or a side of thearray 
        value = arr[middle]
        print(f"middle : {value}")
        if value < target : 
            low = middle + 1 # as we already compared with the middle so we can get rid of that one also
        elif value > target : 
            high = middle - 1

        else :
            return middle   # that means the middle one is the target

        


def main():
    arr = [1,2,3,5,6,7,8,9,12,34,45,46,47,49,51,62,64,67,87,98]
    target = 51
    out = BinarySearch(arr, target)
    print(f"The index of the {target} is {out}")

if __name__ == "__main__":
    main()