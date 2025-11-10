# def MergingArray(arr1, m, arr2,n):
#     if not arr2:
#         return arr1
    
#     if not arr1 :
#         return arr2
    
#     i = m -1
#     j = n -1
#     k = m + n -1

#     while(j >= 0):
#         if i >0 and arr1[i]>arr2[j]: # as it goes till the first index and 
#             arr1[k] = arr1[i]
#             i -= 1

#         else:
#             arr1[k] = arr2[j]
#             j -= 1
#             # temp = arr1[i] #3
#             # arr1[i] = arr2[j]
#             # arr2[j] = temp
#             # j = j +1
        
#         k -= 1

#     return arr1

def MergingArray(nums1, m, nums2, n):
    i = m - 1          # last valid index in nums1
    j = n - 1          # last index in nums2
    k = m + n - 1      # write index at the very end of nums1

    while j >= 0:      # only need to place nums2’s elements
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1


def main():
    nums1 = [2,2,3,0,0,0]
    m = 3
    nums2 = [1,5,6]
    n = 3

    # if nums1[0]<nums2[0]:
    #     print(f"The array is {nums1}")
    # else:
    #     temp= nums1[0]
    #     nums1[0] = nums2[0]
    #     nums2[0] = temp
    #     print(f"The array is {nums1}")


    out = MergingArray(nums1, m, nums2, n)
    print(f"The merginal array is : {out}")

    nums11 = [1]
    m1 = 1
    nums21 = []
    n1 = 0
    out1 = MergingArray(nums11, m1, nums21, n1)
    print(f"The merginal array is : {out1}")

    nums12 = [0]
    m2 = 0
    nums22 = [1]
    n2 = 1
    out2 = MergingArray(nums12, m2, nums22, n2)
    print(f"The merginal array is : {out2}")

if __name__ == "__main__":
    main()