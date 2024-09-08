def modifiedList( nums, head):
    dummy = ListNode(0)  # Create a dummy node to handle edge cases
    dummy.next = head
    prev, curr = dummy, head
    nums_set = set(nums)
    while curr:
        if curr.val in nums_set:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next



