def ShortestPalindrome(s):
    if not s:
        return s

    rev = s[::-1]
    n = len(s)

    # Find the longest prefix of s that is a palindrome.
    # That prefix will match a suffix of rev.
    for i in range(n, -1, -1): # -1 excluding means till 0
        if s[:i] == rev[n - i:]:
            # rev[:n-i] is the reversed suffix we need to prepend.
            return rev[:n - i] + s

    # Fallback (in practice we always return inside the loop)
    return rev


def main():
    s = "aacecaaa"
    out = ShortestPalindrome(s)
    print(f"The shortest palindrome for {s} is {out}")

    s1 = "abcd"
    out1 = ShortestPalindrome(s1)
    print(f"The shortest palindrome for {s1} is {out1}")

if __name__ == "__main__":
    main()