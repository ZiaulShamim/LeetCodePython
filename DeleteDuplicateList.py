class LListNode(object):
    def __init__(self, val, next = None ):
        self.val = val
        self.next = next

def LinkedListToArray(List):
    arr = []
    current = List

    while  current:
        arr.append(current.val)
        current = current.next

    return arr

def ArrayToLindedList(arr):
    if not arr:
        return None
    
    head = LListNode(arr[0])
    current = head # we will return the head of the linkedList that's why we have to have to value into something

    for i in range(1, len(arr)):
        current.next = LListNode(arr[i]) # make another node as the next node of the current node
        current = current.next   # update the current with the next one as in next iteration it doesn't override the current

    return head # return only head of the linked List 


def DeleteDuplicateList(list):
    
    current = list  # head of the linked list

    while (current and current.next):
        if current.val == current.next.val:  # if they are equal then skip that node and go to the next node
            current.next = current.next.next # set the next next node as the next node if they are equal mans skip this next node

        else:
            current = current.next # Asssign the next node as the current node means you include next node value in the new list

    return list # return the same list just delete/ skip the duplicate values !


    

def main():
    head = [1,1,2]
    list = ArrayToLindedList(head)
    out = DeleteDuplicateList(list)
    arr = LinkedListToArray(out)
    print(f"THe list without duplicate is : {arr}")

    head1 = [1,1,2,3,3]
    list1 = ArrayToLindedList(head1)
    out1 = DeleteDuplicateList(list1)
    arr1 = LinkedListToArray(out1)
    print(f"THe list without duplicate is : {arr1}")

if __name__ == "__main__":
    main()