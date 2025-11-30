class ListNode(object):
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

def ListTOArray(list):
    pass

def ArrayToList(arr):
    if not arr:
        return None
    
    head = arr [0]

    current = head
    for val in arr[1:]:
        current.next = ListNode(val) 
        current = current.next

    return head

        


def DelDuplicatefromList(list):
    pass

def main():
    arr = [1,2,3,4,1,6,3,7]
    ArrayTList = ArrayToList(arr)

if __name__ == "__main__":
    main()