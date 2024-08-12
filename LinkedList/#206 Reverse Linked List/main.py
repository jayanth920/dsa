def reverseList(head):
    # Iterative
    prev = None
    curr = head
    while curr:
        new = curr.next
        curr.next = prev
        prev = curr
        curr = new
    return prev

    # Recursive
    # def recurse(prev,curr):
    #     if curr is None:
    #         return prev
    #     new = curr.next
    #     curr.next = prev
    #     return recurse(curr,new)
    # return recurse(None,head)
