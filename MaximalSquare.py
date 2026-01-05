def MaximalSqu1(TDarr):

    max_sqr = 0
    row = len(TDarr)
    column = len(TDarr[0])

    for i in range(row):
        for j in range(column):

            if TDarr[i][j] == "1":
                update_sqr = 1
                k = 1  # how much we expand from (i,j)

                while i + k < row and j + k < column:
                    ok = True

                    # check the new bottom row of the expanded square
                    for x in range(j, j + k + 1):   # for each column(x) of the row (j(0)+k(1)+ 1), next one
                        if TDarr[i + k][x] != "1":  # row change one time only byt the x(column change every time )
                            ok = False
                            break

                    # check the new right column of the expanded square
                    if ok:  # if all the value in the next row is 1 then we will check otherwise we do not even have to check
                        for y in range(i, i + k):  # for each row(y) of the the column(i+k) 
                            if TDarr[y][j + k] != "1":  # Only row change for same column (j+k)
                                ok = False
                                break

                    if not ok:  # if both row and column are not with values of 1's
                        break

                    update_sqr += 1
                    k += 1

                if max_sqr < update_sqr:
                    max_sqr = update_sqr

    return max_sqr * max_sqr  # area

def MaximalSqu(TDarray):
    row = len(TDarray)
    column = len(TDarray[0])

    # make the data frame for store the square value 
    dp = [[0]*(column+1) for _ in range(row + 1)]  # One row and column bigger than the original TDarray if you want you can make it like the same but have to work little more 

    max_side = 0

    for i in range(1, row+1): # start assigning the first row and column as (1,1) as it doesn't give you error after negate 1 from the row and column when go backword
        for j in range(1, column+1):
            if TDarray[i-1][j-1] == "1":  # start from (1,1)
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])  # for the first element(1,1) it's already 1 as 1+ and rest three is 0 so that is only 1 for the (0,0) cell of the main 2Darray
                if dp[i][j] > max_side:
                    max_side = dp[i][j]

    return max_side*max_side

def main():
    TDarray = [["1","0","1","0","0"],
               ["1","0","1","1","1"],
               ["1","1","1","1","1"],
               ["1","0","0","1","0"]]
    
    # for line in TDarray:
    #     print(line)

    print(f"The row of the 2D array is {len(TDarray)}")
    print(f"The column of the 2D array is {len(TDarray[0])}")

    maxSqr = MaximalSqu(TDarray)

    print(f"The maximum square of the Areas with the 1 value is : {maxSqr}")

if __name__ == "__main__":
    main()