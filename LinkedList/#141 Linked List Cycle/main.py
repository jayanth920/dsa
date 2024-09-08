class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
        walker = head
        runner = head
        while runner.next != None and runner.next.next != None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False




# TEST CASES
tests = [
    ([3, 2, 0, -4], 1),  # Expected: True
    ([1, 2], 0),         # Expected: True
    ([1], -1),           # Expected: False
    ([], -1),            # Expected: False
    ([1], 0),            # Expected: True
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4),  # Expected: True
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1)  # Expected: False
]



# TEST CASE RUNNER BELOW (IGNORE) --------------
# Helper function to create linked list and introduce a cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]

    # Create linked list
    for val in values[1:]:
        new_node = ListNode(val)
        nodes.append(new_node)
        current.next = new_node
        current = new_node
    
    # Introduce cycle if pos is valid
    if pos != -1:
        current.next = nodes[pos]
    
    return head

# Instantiate the solution
solution = Solution()

# Run and print test cases
for i, (values, pos) in enumerate(tests):
    head = create_linked_list_with_cycle(values, pos)
    result = solution.hasCycle(head)
    print(f"Test Case {i + 1}: {result}")
