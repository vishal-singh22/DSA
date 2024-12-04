# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify result list construction
        curr = dummy  # Pointer to traverse and build the new list
        carry = 0  # Carry to store overflow from digit addition

        # Loop until there are no more nodes to process or carry to add
        while carry or l1 or l2:
            if l1:
                carry += l1.val  # Add the current node's value from l1
                l1 = l1.next  # Move to the next node in l1
            if l2:
                carry += l2.val  # Add the current node's value from l2
                l2 = l2.next  # Move to the next node in l2

            curr.next = ListNode(carry % 10)  # Create a new node with the current digit
            carry //= 10  # Update carry for the next iteration
            curr = curr.next  # Move to the next node in the result list

        return dummy.next  # Return the head of the new list
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create linked lists
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Add the two numbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result
print_linked_list(result)
