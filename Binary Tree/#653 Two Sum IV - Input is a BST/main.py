# Fastest !! - EXCELLENT SOLN
# def findTarget(root, k):
#     seen = set()
#     def find(node):
#         if node is None:
#             return False
#         if k - node.val in seen:
#             return True
#         seen.add(node.val)
#         return find(node.left) or find(node.right)
#     return find(root)

# THIS IS ALSO EXCELLENT
# def findTarget(root, k):
#         def traverse(node):
#             if not node:
#                 return []
#             return traverse(node.left) + [node.val] + traverse(node.right)
        
#         nums = traverse(root)
#         x, y = 0, len(nums) - 1

#         while x < y:
#             sum = nums[x] + nums[y]
#             if sum == k:
#                 return True
#             elif sum < k:
#                 x += 1
#             else:
#                 y -= 1
#         return False
    
# THIS IS ALSO ANOTHER METHOD EXCELLENT
# def findTarget(root, k):
#         def traverse(node):
#             if not node:
#                 return []
#             return traverse(node.left) + [node.val] + traverse(node.right)
        
#         nums = traverse(root)
#         my = set()
#         for i in range(len(nums)):
#             target = k - nums[i]
#             if target in my:
#                 return True
#             else:
#                 my.add(nums[i])
#         return False