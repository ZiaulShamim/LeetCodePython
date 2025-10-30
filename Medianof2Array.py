def MedianOf2Array(arr1, arr2):
    total_len = len(arr1) + len(arr2)
    indecies = (total_len+1)//2

    length1 = len(arr1)
    length2 = len (arr2)
    total_in = length1+ length2 

    if (total_in == 0):
        return 0
    
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

    newArr = []
    for i in range(0,indecies):
        if (arr1[i]<arr2[i]):
            newArr.append(arr1[i ])
        else:
            pass


def main():
    arr1 = [1,3,5,6,8]
    arr2 = [2,3,4,5]
    Output = MedianOf2Array(arr1, arr2)
    print(f"The median of two array is {Output}")

if __name__ == "__main__":
    main()