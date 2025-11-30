def Sum3(num):
    num.sort()

    n = len(num)
    res = []

    for i in range(n):
        if i > 0 and num[i] == num[i-1]:
            continue

        target = -num[i]  # as total have to be 0 so negate the number
        l = i + 1
        r = n-1

        while l< r:
            s = num[l] + num[r]

            if s == target :
                res.append([num[i], num[l], num[r]])

                l += 1   # To move the pointer
                r -= 1 

                while l < r and num [l] == num[l-1]:
                    l += 1

                while l <r and num[r] == num[r+1]:
                    r -= 1

            elif   s < target: # Need bigger sum of the target -> move left pointer
                l += 1

            else:
                r -= 1  # s. target -> need a smaller sum -> move right pointer

            

    return res


def main():
    nums = [-1,0,1,2,-1,-4]
    out = Sum3(nums)
    print(f"The combinatins are {out}")

    nums1 = [0,1,1]
    out1 = Sum3(nums1)
    print(f"The combinatins are {out1}")


    nums2 = [0,0,0]
    out2 = Sum3(nums2)
    print(f"The combinatins are {out2}")


if __name__ == "__main__":
    main()