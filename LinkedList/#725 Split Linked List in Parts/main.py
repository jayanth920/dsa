def solve(head,k):
        n = 0
        p = head
        while p:
            p = p.next
            n += 1

        res = []

        part_size = n // k
        num_xtra_parts = n % k

        current = head
        for i in range(k):
            current_part_size = part_size + (1 if num_xtra_parts > 0 else 0)
            if num_xtra_parts > 0:
                num_xtra_parts -= 1

            part_head = current
            for j in range(current_part_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            res.append(part_head)

        while len(res) < k:
            res.append(None)

        return res
