#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    head = ListNode()
    cur = head
    carry = 0
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.p1 = l1
        self.p2 = l2
        while (self.p1 != None) or (self.p2 != None):
            self.x = self.p1.val if (self.p1 != None) else 0
            self.y = self.p2.val if (self.p2 != None) else 0
            self.sum = self.x + self.y + self.carry
            self.carry = int(self.sum / 10)
            self.sum = int(self.sum % 10)
            self.cur.next = ListNode(self.sum)
            self.cur = self.cur.next
            self.p1 = self.p1.next if (self.p1 != None) else None
            self.p2 = self.p2.next if (self.p2 != None) else None

        if (self.carry):
            self.cur.next = ListNode(1)

        return self.head.next

def main():
    s = Solution()
    l1 = ListNode(3, ListNode(4))
    l2 = ListNode(5, ListNode(6))
    solution = s.addTwoNumbers(l1, l2)
    while (solution is not None):
        print (solution.val)
        solution = solution.next

if __name__ == "__main__":
    main()               
            
        
# @lc code=end

