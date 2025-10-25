class ListNode(object):
    def __init__(self,val=0,next =None):
        self.val = val
        self.next = next

class DLListNode(object):
    def __init__(self, val, next= None, previous = None, index= None):
        self.val = val
        self.next = next
        self.previous = previous
        self.index = index
        

def create_linkedList(arr):
    if not arr :
        return None
    head = ListNode(arr[0])
    current = head 
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def printingLL(head):
    current = head
    while current:
        print(current.val, end= "->" if current.next else "\n") 
        current = current.next

def main():
    arr1 = [1,2,2,1]
    arr2 = [1,2]
    head = create_linkedList(arr1)
    printingLL(head)
    #print(head)  # You can't print the whole head by using the print option 

if __name__ == "__main__":
    main()