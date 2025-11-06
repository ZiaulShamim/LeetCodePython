def NonDuplicateLen(arr):

    if not arr :
        return 0
    set1 = set()
    for i in range(0, len(arr)):
        set1.add(arr[i])

    return len(set1)

# By using the hashMap as well 

# Using the pointer method 
def removeDuplicate(arr):
    if not arr :
        return 0 
    
    i = 1 # Pointer will tracks where the next unique element should go
    for j in range(1, len(arr)):
        if arr[j] != arr[j -1]:  # as the array are sorted already so you can check only previous vale with it and 
            # as it will be true only for the first case of a unique number so, increase i by 1
            arr[i] = arr[j]  # By using this line we are making a new array with only the unique element as i only change when it's unique
            i = i+ 1

    return i

# If you want to return only unique part of the array by using i 
def unique_only(arr):
    if not arr:
        return []
    
    result = [arr[0]]  # first element is always unique
    for j in range(1, len(arr)):
        if arr[j] != arr[j - 1]:
            result.append(arr[j])
    return result



    

def main():
    nums = [1,1,2]
    out1 = NonDuplicateLen(nums)
    print(f"The non duplicate length of [1,1,2] is {out1}")

    nums1 = [0,0,1,1,1,2,2,3,3,4]
    out2 = NonDuplicateLen(nums1)
    print(f"The non duplicate length of [0,0,1,1,1,2,2,3,3,4] is {out2}")

   
if __name__ == "__main__":
    main()