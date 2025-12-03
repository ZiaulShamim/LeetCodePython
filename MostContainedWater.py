def MostContainedWater(arr):
    # we have to find the most contain water jar from the array with their height(index- value) and weidth(width - indecies distance)
    updatArea = 0
    for i in range(0, (len(arr)-1)):
        for j in range (1, len(arr)):
                if arr[i]<arr[j]:
                    height = arr[i]  # It should the the minimum of the two index or either one if they are equal
                elif arr[j]<arr[i]:
                    height = arr[j]
                else :
                     height = arr[i]
                weidth = j -i# To make the width there should be two pointer because that is the distance between them

                area = height*weidth

                if area >updatArea:
                     updatArea = area

                j += 1
        
        i += 1

    return updatArea

def main():
    height = [1,8,6,2,5,4,8,3,7]
    out = MostContainedWater(height)
    print(f"The most containable water for this array is {out}")

    height = [1,1]
    out = MostContainedWater(height)
    print(f"The most containable water for this array is {out}")

if __name__ == "__main__":
    main()