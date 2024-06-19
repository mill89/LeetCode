# Определение класса для односвязного списка.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        # Перемещаем быстрый указатель на два шага, а медленный на один шаг каждый раз.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Когда быстрый указатель достигнет конца, медленный будет в середине.
        return slow
