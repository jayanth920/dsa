# O(n)
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            
            current.next = ListNode(sum % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next
        
        