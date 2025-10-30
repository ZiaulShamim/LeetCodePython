def findDisappearedNumbers(arr):
        # num = i+1
        # how about that we make a new array and if we see that number then we pop that number from that array??
        mydic = {i :None for i in  range(1,(len(arr)+1))}
        for value in arr:
                if value in mydic :
                        mydic[value].append[value]

        empty_keys = []

        for key, value in mydic.items():
            if not value:      # checks for empty list, empty string, None, etc.
                empty_keys.append(key)

        return empty_keys

        

def main():
        arr1 = [4,3,2,7,8,2,3,1]
        arr2 = [1,1]

        Out1 = findDisappearedNumbers(arr1)
        Out2 = findDisappearedNumbers(arr2)

        print(Out1)
        print(Out2)

if __name__ =="__main__":
        main()