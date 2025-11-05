def bisect_left(arr, target):
    left = 0
    right = len(arr)

    while(left <right):  # [1,3,5,6]
        mid = (left +right)//2

        if arr[mid] <target:
            left = mid + 1
        else:
            right = mid

    return left

def FindIndecies1(arr, target):
    if len(arr) == 0:
        return 
    
    j = 0
    for i, num in enumerate(arr):
        if target <= num:
            return i
    return len(arr)

def FindIndecies11(arr, target):
    i = bisect_left(arr, target)
    return i if i <len(arr) and arr[i] == target else len(arr)
    
    

def main():
    nums = [1,3,5,6]
    target = 5
    Out = FindIndecies1(nums, target)
    print(f" The target is in indecies {Out}")


    nums1 = [1,3,5,6]
    target1 = 2
    Out1 = FindIndecies1(nums1, target1)
    print(f" The target is in indecies {Out1}")

    nums2 = [1,3,5,6]
    target2 = 7
    Out2 = FindIndecies1(nums2, target2)
    print(f" The target is in indecies {Out2}")

if __name__ == "__main__":
    main()