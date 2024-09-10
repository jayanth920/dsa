class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    # def gcd(x, y):
    #     while y != 0:
    #         (x, y) = (y, x % y)
    #     return x

    # walker = head
    # runner = head.next
    # if runner == None:
    #     return head

    # while runner:
    #     new = ListNode(gcd(walker.val, runner.val))
    #     walker.next = new
    #     new.next = runner

    #     walker = new.next
    #     runner = runner.next
    # return head
    
    # Using a single pointer. - Not much difference in speed.
    if not head.next:
        return head
    runner = head
    while runner.next:
        new = ListNode(gcd(runner.val, runner.next.val))
        new.next = runner.next
        runner.next = new
        runner = new.next
    return head
