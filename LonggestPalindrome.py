def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


def LongestPalindrome(s):
    longest = ""

    for i in range(len(s)):
        
        right = left = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        even = s[left+1:right]
        

        lefto = i
        righto = i+1
        while lefto >= 0 and righto < len(s) and s[lefto] == s[righto]:
            lefto -= 1
            righto += 1

        odd = s[lefto+1:righto]

        if(len(odd)>len(longest)):
            longest = odd
        if(len(even)> len(longest)):
            longest = even

        

    return longest



def main():
    s = "babad"
    out = LongestPalindrome(s)
    print(f"The longest palindrome for {s} is {out}")

    s1 = "cbbd"
    out1 = LongestPalindrome(s1)
    print(f"The longest palindrome for {s1} is {out1}")

if __name__ == "__main__":
    main()