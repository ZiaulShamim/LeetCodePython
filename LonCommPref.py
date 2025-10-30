## Doing in a horizontatl scanning

def LongestCommonPrefix(arr):
    first= arr[0]
    for str in arr:
        pass
    
# DOing in a Binary Search way
def LongestBin(args):
    if not args:
        return ""

    min_len = min(len(s) for s in args)   # Isn't it the x2 because we find the length and then find the minimum

    def is_common(length):
        prefix = args[0][:length] 
        return all(s.startswith(prefix))


def main():
    arr1 = ["flower","flow","flight"]
    LongestCommonPrefix(arr1)

    if not arr1:
        return ""

    min_len = min(len(s) for s in arr1)   # Isn't it the x2 because we find the length and then find the minimum
    print(min_len)  #4

    def is_common(length):
        prefix = arr1[0][:length] # fl
        
        return all(s.startswith(prefix))
    
    low, high = 0, min_len

    while low < high:
        mid = (low + high + 1)// 2
        print(mid)  # 2 
        if is_common(mid):
    #         low = mid
    #     else : 
    #         high = mid - 1
    #     return arr1[0][:low]



if __name__  == "__main__":
    main()