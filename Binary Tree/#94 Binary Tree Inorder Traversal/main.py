def inorderTraversal(root):
    res = []

    def treeTraversal(node):
        if node is None:
            return
        treeTraversal(node.left)
        res.append(node.val)
        treeTraversal(node.right)

    treeTraversal(root)
    return res
