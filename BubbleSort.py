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

def main ():
    arr = [1,4,6,7,3,4,9,1,6,12]
    out = BubbleSort(arr)
    print(f"The sorted array is {out}")

if __name__ == "__main__":
    main()