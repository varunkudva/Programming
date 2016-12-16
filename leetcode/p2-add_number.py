class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lnew = ListNode(0)
        carry_over = 0
        if l1.next != None and l2.next != None:
            lnew.next, carry_over = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next == None:
            if l2.next:
                lnew.next, carry_over = self.addTwoNumbers(l1, l2.next)

        val = l1.val + l2.val + carry_over
        if val >= 10:
            lnew.val = val % 10
            carry_over = val / 10
        else:
            lnew.val = val
            carry_over = 0
        return lnew, carry_over

def read_number(num_str):
    prev = None
    curr = None
    num_str = num_str.strip().strip('(').strip(')').split('->')
    for c in num_str:
        curr = ListNode(int(c))
        if prev:
            prev.next = curr
        else:
            prev = curr
            # first node
            l1 = curr

    return l1


if __name__ == '__main__':
   a, b = raw_input().split('+')
   l1 = read_number(a)
   l2 = read_number(b)
   lnew, carryover = Solution().addTwoNumbers(l1, l2)
   if carryover:
       new_head = ListNode(carryover)
       new_head.next = lnew
       lnew = new_head

   sumlist = list()
   while lnew:
       sumlist.append(str(lnew.val))
       lnew = lnew.next

   print "->".join(sumlist)



