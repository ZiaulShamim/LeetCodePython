def RemoveEle(arr, tar):
    if not arr:
        return 0
    
    i = 0
    for j in range(0, len(arr)):
        if (arr[j] != tar):
            arr[i] = arr[j]
            i += 1

    return i 

def main():
    nums = [3,2,2,3]
    val = 3
    out = RemoveEle(nums, val)
    print(f"The length after deleting item is : {out}")

    nums1 = [0,1,2,2,3,0,4,2]
    val1 = 2
    out1 = RemoveEle(nums1, val1)
    print(f"The length after deleting item is : {out1}")

if __name__ == "__main__":
    main()