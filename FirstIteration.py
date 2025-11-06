def FIrstIteration(str1, str2):
    if not (str1 or str2):
        return -1

    m, n = len(str1), len(str2)

    if m<n :
        return -1
    
    index = m -n +1 # To go till 1 more index then the length of the niddle becasue it would not be possible that with less indecis 
    # it could make the word with more length and another thing is it will break the loop for if statement as i+m would break the limit\
    
    for i in range(index):
        if str1[i:i+n] == str2:
            return i                # ← return immediately = first occurrence
    return -1
    


def main():
    haystack = "sadbutsad"
    needle = "sad"
    out = FIrstIteration(haystack, needle)
    print(f"The itteration occured in the very first time is at index : {out}")


    haystack1 = "leetcode"
    needle1 = "leeto"
    out1 = FIrstIteration(haystack1, needle1)
    print(f"The itteration occured in the very first time is at index : {out1}")

if __name__== "__main__":
    main()