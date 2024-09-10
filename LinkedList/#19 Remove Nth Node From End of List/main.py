def solve(head, n):
    # This is Two pass method. Inital version I did.
    # p = head
    # actual_len = 0

    # while p:
    #     p = p.next
    #     actual_len += 1

    # res_len = actual_len - n

    # if n == actual_len:
    #     c = head
    #     tmp = c.next
    #     c.next = None
    #     head = tmp
    #     return head

    # curr = head
    # counter = 1

    # while counter != res_len and curr:
    #     counter += 1
    #     curr = curr.next

    # temp = curr.next.next
    # lost = curr.next
    # lost.next = None
    # curr.next = temp

    # return head
    
    
    # 2 POINTERS - 1 PASS
        walker = head
        runner = head
        k = n

        while k > 0:
            runner = runner.next
            k -= 1

        if not runner:
            return head.next

        while runner.next:
            walker = walker.next
            runner = runner.next

        walker.next = walker.next.next

        return head

# TEST CASES
test_cases = [
    ([1, 2, 3, 4, 5], 2),
    ([1, 2], 2),
    ([1], 1),
    ([1, 2, 3, 4], 1),
    ([1, 1, 1, 1, 1], 3),
    ([i for i in range(1, 1001)], 500),
    ([1, 2, 3], 1),
    ([3, 3, 3, 3, 3], 4),
]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)



for values, n in test_cases:
    head = build_list(values)
    print(f"Original list: {values}, n = {n}")
    new_head = solve(head, n)
    print("Modified list:", end=" ")
    print_list(new_head)
