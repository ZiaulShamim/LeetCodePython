# Bubble sort is a brut-force approach to sort an array 
# for all the elements it checks if this is the smaller number than others
def BubbleSort(arr):
    n = len(arr)-1
    for i in range(0, n-1):
       
        for j in range(i+1, n):
            if arr [i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

# Insertion sort is quite opposite than the bubble sort 
# Instead of comparing the value from the next index sort the previous sorted with the current index
def InsretionSort(arr):
    n = len(arr) - 1
    for i in range(1, n):
        temp = arr[i]

        j = i - 1

        while(j >= 0 & arr[j] > temp ):
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = temp


    return arr

def main ():
    arr = [4,1,6,7,3,4,9,1,6,12]
    out = BubbleSort(arr)
    print(f"The sorted array is {out}")

    out2 =InsretionSort(arr)
    print(f"The Sorted array after Insertion Sort is {out2}")

if __name__ == "__main__":
    main()