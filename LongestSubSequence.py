def LongestCommonSubsequence(x, y):
    m, n = len(x), len(y)

     # making a 2D array of characters set for both string values with their size
    Ics_Table  = [[0 for _ in range(n+1)] for _ in range(m+1)]

    max_len = 0 # to keep track of the longest subsequence
    max_row = 0 
    max_col = 0

    # initialize first row with 0 and columns with 0 as well
    # In hava this is needed but in python this is not necessary

    # Fill the ICS Table 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1] :
                Ics_Table[i][j] = 1 + Ics_Table[i-1][j-1]
                if max_len < Ics_Table[i-1][j-1] :
                    max_len = Ics_Table[i][j]

                    max_row =i
                    max_col = j
            else :
                Ics_Table[i][j] = max(Ics_Table[i-1][j], Ics_Table[i][j-1])


    # Longest common Subsequence 
    
    longest_Subsequence = []

    while max_row >= 1 and max_col >= 1 :
        if x[max_row - 1] == y[max_col -1] :
            longest_Subsequence.append(x[max_row - 1])
            max_row -= 1
            max_col -= 1
        elif Ics_Table[max_row -1][max_col] >= Ics_Table[max_row][max_col - 1] :
            max_row -= 1
        else :
            max_col -= 1
    return "".join(reversed(longest_Subsequence))


a = "instagram"
b = "instrantgrammar"

def main():
    print("This is the main function")
    long_subsequence = LongestCommonSubsequence(a,b)
    print(f"The longest common subsequence is : {long_subsequence}")

if __name__ == "__main__":
    main()
