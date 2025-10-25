def FindMedianof2Array(A1, A2):
    total_length = len(A1) + len(A2)

    if total_length == 0:
        return 0
    
    elif total_length % 2 == 0:  # if the total length is even 
        med_in1 = total_length//2
        med_in2 = (total_length//2) + 1
        # 
        if med_in1 <= len(A1):
            med_num1 = A1[med_in1 -1]
        else :
            secArrIn = med_in1 -len(A1)
            med_num1 = A2[secArrIn -1]

        if med_in2  <= len(A1):
            med_num2 = A1[med_in2 -1]
        else :
            secArrIn = med_in2 -len(A1)
            med_num2 = A2[secArrIn -1]
        total = (med_num1 + med_num2)/2

        return total
    
    else :   # If the total number is odd
        med_in = int((total_length/2) +1)
        if med_in  <= len(A1):
            ins = (med_in -1 )
            median = A1[ins]
        else :
            secArrIn = med_in -len(A1)
            ins1 = secArrIn -1
            median = A2[ins1]

        return median

def findKthElement(A, B, k):
    if not A: return B[k-1]
    if not B: return A[k-1]
    if k == 1: return min(A[0], B[0])

    i = min(len(A), k // 2)
    j = k - i

    if A[i - 1] < B[j - 1]:
        return findKthElement(A[i:], B, k - i)
    else:
        return findKthElement(A, B[j:], k - j)

def findMedianSortedArrays_logNplusM(nums1, nums2):
    total = len(nums1) + len(nums2)
    if total % 2 == 1:
        return findKthElement(nums1, nums2, total // 2 + 1)
    else:
        return (findKthElement(nums1, nums2, total // 2) +
                findKthElement(nums1, nums2, total // 2 + 1)) / 2


def main():
    array1 = [1,3]
    array2 = [2]

    out1 = FindMedianof2Array(array1, array2)
    print(out1)
    print("This is main function.")

    out2 = findMedianSortedArrays_logNplusM(array1, array2)
    print(f" This is the median output of the Leetcode : {out2}")

if __name__ == "__main__":
    main()

