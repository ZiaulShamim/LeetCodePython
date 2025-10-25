def LongestCommonSubsequence(x, y):
    m, n = len(x), len(y)

    # Create a 2D table initialized with 0s
    Ics_Table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the LCS Table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                Ics_Table[i][j] = Ics_Table[i - 1][j - 1] + 1
            else:
                Ics_Table[i][j] = max(Ics_Table[i - 1][j], Ics_Table[i][j - 1])

    # Trace back to build the LCS string
    i, j = m, n
    longest_Subsequence = []

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            longest_Subsequence.append(x[i - 1])
            i -= 1
            j -= 1
        elif Ics_Table[i - 1][j] >= Ics_Table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(longest_Subsequence))


# Example input strings
a = "instgram""instrantgrammar"
b = "instagram"

def main():
    print("This is the main function")
    long_subsequence = LongestCommonSubsequence(a, b)
    print(f"The longest common subsequence is: {long_subsequence}")

if __name__ == "__main__":
    main()
