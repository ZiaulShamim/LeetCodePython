def MaximalSqu(TDarr):

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
                    for x in range(j, j + k + 1):
                        if TDarr[i + k][x] != "1":
                            ok = False
                            break

                    # check the new right column of the expanded square
                    if ok:
                        for y in range(i, i + k):
                            if TDarr[y][j + k] != "1":
                                ok = False
                                break

                    if not ok:
                        break

                    update_sqr += 1
                    k += 1

                if max_sqr < update_sqr:
                    max_sqr = update_sqr

    return max_sqr * max_sqr  # area


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