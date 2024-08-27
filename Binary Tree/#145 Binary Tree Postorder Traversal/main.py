# Recursive

# def postorderTraversal(root):
#         res = []
#         def treeTraversal(node):
#             if node is None:
#                 return
#             treeTraversal(node.left)
#             treeTraversal(node.right)
#             res.append(node.val)
#         treeTraversal(root)
#         return res


#  Iteratively - using STACK
def postorderTraversal(root):
    if not root:
        return []

    stack = [root]
    output = []

    while stack:
        node = stack.pop()
        output.append(node.val)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return output[::-1]