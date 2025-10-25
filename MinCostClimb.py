def MinCostClimb(arr):
    add1 = 0 # To ckeck that after added the value of 1 step 
    add2 = 0 # Tp ckeck the value after added the value 2 step

    if (len(arr) ==1) :
        return arr[0]
    
    # for index 1, 2 and 3  make it specific 
    if (len(arr == 2)):
        if (arr[0]< arr[1]):
            return arr[0]
        
    if (len(arr == 3)):
        if 4
    
    for i in range(0,len(arr)):

        if (arr[0]< arr[1]) :

        add1 = arr[i] + arr[i+1]
        add2 = arr[i+ 1] + arr[i+2]

        if (add1 > add2)

## Rather than use we can use case I think becaue I could have multiple case then 



def main():
    arr1 = [10,15,20]
    arr2 = [1,100,1,1,1,100,1,1,100,1]

    min1 = MinCostClimb(arr1)
    min2 = MinCostClimb(arr2)
    print(f"The Min cost to climb the stairs for arr1 is {min1}")
    print(f"The Min cost to climb the stairs for arr2 is {min2}")



if __name__ == "__main__":
    main()