def LongestCommonPri(arr):

    if len(arr)==0:
        return
    if len(arr)==1:
        return arr[0]
    else:
        example = arr[0]
        
        for word in arr[1:]:
            j = 0
            while (j<len(example) and j<len(word) and (example[j] == word[j])):
                j = j + 1

            example = example[:j]
            if not example:
                return ""
        return example
    
# another way more time efficient 
def LongestCommonPri1(arr):
    if not arr :
        return 
    
    s1 = min(arr) # Lexicographically smallest 
    s2 = max(arr) # Lexicographically largest

    i = 0
    n = min(len(s1), len(s2))

    while (i<n and s1[i] == s2[i]):
        i = i + 1


    return s1[:i]
    


def main ():
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]

    Out1 = LongestCommonPri(strs)
    Out2 = LongestCommonPri(strs2)

    print(f"The longest common prefix is : {Out1}")
    print(f"The longest common prefix is : {Out2}")

    Out3 = LongestCommonPri1(strs)
    Out4 = LongestCommonPri1(strs2)

    print(f"The longest common prefix is : {Out3}")
    print(f"The longest common prefix is : {Out4}")



if __name__ == "__main__":
    main()