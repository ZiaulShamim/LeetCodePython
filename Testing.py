def findKthElement(A, B, k):
    if not A: return B[k-1]   # If the array A is empty then return the element from B array
    if not B: return A[k-1]
    if k == 1: return min(A[0], B[0]) # If the keth value is just one, from either way of odd and even median number 

    i = min(len(A), k // 2)  # find the minimum between the length of a and Kth devided 2 (if k =2) i = 1
    j = k - i  # 2 - 1 

    if A[i - 1] < B[j - 1]:
        return findKthElement(A[i:], B, k - i)
    else:
        return findKthElement(A, B[j:], k - j)

def findMedianSortedArrays_logNplusM(nums1, nums2):
    total = len(nums1) + len(nums2)

    if total % 2 == 1:   # If the length of the two arrays  is odd
        return findKthElement(nums1, nums2, total // 2 + 1)
    else:     # If the length is even 
        return (findKthElement(nums1, nums2, total // 2) +
                findKthElement(nums1, nums2, total // 2 + 1)) / 2
    

def main():
    array1 = [1,3]
    array2 = [2,5]
    findthe_Keth = findKthElement(array1, array2,3)
    print(f"The keth element is : {findthe_Keth}")


if __name__ == "__main__":
    main()