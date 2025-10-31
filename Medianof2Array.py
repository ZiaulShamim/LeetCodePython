def MedianOf2Array(arr1, arr2):
    length1, length2 = len(arr1), len(arr2)
    total_len = length1 + length2
    if total_len == 0:
        return 0  # or raise ValueError

    i = j = 0
    prev = curr = None
    target = total_len // 2  # stop when we've taken target+1 items

    for _ in range(target + 1):
        prev = curr
        # Take from arr1 if it has elements AND (arr2 is exhausted OR arr1[i] <= arr2[j])
        if ((i<length1 and j>=length2) or (i<length1 and arr1[i]<=arr2[j])): #First array is not empty(all not checked) and second array is empty
            #   or First array is not empty(all not checked) and element in 1st array is less then element in 2nd array
            curr = arr1[i]
            i += 1
        else:
            # If the element not select from 1st array select from second array
            curr = arr2[j]
            j += 1

    if total_len % 2 == 1:      # odd -> middle element
        return curr
    else:                       # even -> average of two middle elements
        return (prev + curr) / 2

    
    # elif (total_in % 2 == 0):
    #     indecis1 = total_in //2
    #     indecis2 = (total_in // 2) + 1

    #     if indecis1 <= length1 :
    #         median1 = arr1[indecis1 -1]
    #     else: 
    #         indecisSec1 = indecis1 -length1
    #         median1 = arr2[indecisSec1 -1]

    #     if indecis2 <= length1 :
    #         median2 = arr1[indecis2 -1]
    #     else: 
    #         indecisSec2 = indecis2 -length1
    #         median2 = arr2[indecisSec2 -1]

    #     medianev = (median1 + median2) // 2
    #     return medianev

    # else:
    #     indecis = (total_in +1) // 2
        
    #     if indecis <= length1 :
    #         median = arr1[indecis -1]
    #     else: 
    #         indecisSec = indecis -length1
    #         median = arr2[indecisSec -1]
            
    #     return median

    # newArr = []
    # for i in range(0,indecies):
    #     if (arr1[i]<arr2[i]):
    #         newArr.append(arr1[i ])
    #     else:
    #         pass


def main():
    arr1 = [1,3,5,6,8]
    arr2 = [2,3,4,5,9]
    Output = MedianOf2Array(arr1, arr2)
    print(f"The median of two array is {Output}")

if __name__ == "__main__":
    main()