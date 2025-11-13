class TreeNode(object):
    def __init__(self, val =0, leftN = None, rightN = None):
        self.val = val
        self.rightN = rightN
        self.leftN = leftN

def Insert(root, val):
    if val == None:
        return root
    if root is None:
        return TreeNode(val)
    elif(val < root.val):
        root.leftN = Insert(root.leftN, val)  # root.left now becoming the new root
    else:
        root.rightN = Insert(root.rightN,val)  # root.right now becoming the new root

    return root


def BinaryInsert(arr):

    root = None

    for i in range(0, len(arr)):
        root = Insert(root, arr[i])

    return root


def BinInOrdTra(root):
    if root == None:
        return []
    return BinInOrdTra(root.leftN) + [root.val] + BinInOrdTra(root.rightN) 

def main():
    arr = [1,2,3]
    root = BinaryInsert(arr)
    out = BinInOrdTra(root)
    print(out)

    arr1 = [1,2,4,10,5,8, 6,7,9,3]
    root1 = BinaryInsert(arr1)
    out1 = BinInOrdTra(root1)
    print(out1)



if __name__ == "__main__":
    main()