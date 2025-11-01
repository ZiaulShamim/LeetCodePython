class ListNode(object):
    def __init__(self, val =0 ,next_Node = None):
        self.val = val
        self.next = next_Node  # Whatever is assigned with self will work like a method or like a global veriable
        

def ArrayToLList(arr):
    dummy = ListNode()
    tail = dummy

    for val in arr:
        tail.next = ListNode(val) # Put the value in the tail
        tail = tail.next # and make the tail empty again


    return dummy.next # as it will return the whole dummy list


def LListToArr(list):
    arr = []
    while list:  # as long as the list has the node value
        arr.append(list.val)   # put the value in the array
        list = list.next   # go to the next node 

    return arr

def MergeTwoSortedArr(list1, list2):
    dummyList = ListNode()
    tail = dummyList

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next # after putting the value in the tail update the tail of the new list

    # Now when equal indexes of both list doen with comparing now add the rested value from the larger one
    tail.next = list1 or list2  # as far one or both should be doen , so only one with value will be added 

    return dummyList.next


def main():
    arr1 = [1,2,4]
    arr2 = [1,3,4]
    list1 = ArrayToLList(arr1)
    list2 = ArrayToLList(arr2)

    Outa = MergeTwoSortedArr(list1, list2)
    Out1 = LListToArr(Outa)
    print(f"The output of the [1,2,4] and [1,3,4] is  {Out1}")

    arr3 = []
    arr4 = []
    list3 = ArrayToLList(arr3)
    list4 = ArrayToLList(arr4)
    Outb = MergeTwoSortedArr(list3, list4)
    Out2 = LListToArr(Outb)
    print(f"The output of the [] and [] is  {Out2}")


    arr5 = []
    arr6 = [0]
    list5 = ArrayToLList(arr5)
    list6 = ArrayToLList(arr6)
    Outc = MergeTwoSortedArr(list5, list6)
    Out3 = LListToArr(Outc)

    print(f"The output of the [] and [0] is  {Out3}")


if __name__ == "__main__":
    main()