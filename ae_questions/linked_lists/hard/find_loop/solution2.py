"""
Write a function that takes the head of a singly-linked list and returns the node at the origin of the loop where the loop begins.

For example, ```find_loop``` should return Node(4) when running on a singly list structured as follows:

  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                      |         |
                      9 <- 8 <- 7


NOTE: This approach is referred to as the Floyd's Cycle-Finding ("Tortoise and the Hare") Algorithm. With mathematical proofs, it can be proven that the origin node in a cycle of a linked list will be a multiple of origin-head nodes away from the head node. In the above example of 10 nodes, the tortoise and hare pointers meet at node 6, which is exactly 1(4 - 0) nodes away from node 4.

* Explanation *
  - create 2 pointers -- one slow, one fast.
  - while not equal to each other, increment the slow pointer by 1 through the list, and the fast pointer by 2.
  - when the pointers arrive at the same node, exit the loop.
  - reset the slow pointer to the head node.
  - while the slow and fast pointers aren't at the same node, increment them each by 1.
  - return the meeting node, which is the origin node of the loop.

TC: O(n) -- need to loop all the way through until the item with a string value is found. Then loop back until you find that node again, changing all node values back into ints along the way.
SC: O(1) -- no changes to amount of storage, proportional to number of nodes.
"""
class Node:
  def __init__(self, value, nxt):
    self.value = value
    self.next = nxt

def find_loop(head):
  slow, fast = head.next, head.next.next
  while slow != fast:
    slow, fast = slow.next, fast.next.next

  slow = head
  while slow != fast:
    slow, fast = slow.next, fast.next

  return slow

if __name__ == "__main__":
  # holding data structure for nodes
  dict = {}

  nodes = [
    {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": "6", "value": 5},
    {"id": "6", "next": "7", "value": 6},
    {"id": "7", "next": "8", "value": 7},
    {"id": "8", "next": "9", "value": 8},
    {"id": "9", "next": "4", "value": 9}
  ]

  for node in nodes:
    node_value, next_node = node["value"], int(node["next"])
    dict[node_value] = Node(node_value, next_node)

  for value in dict:
    next_node = dict[value].next
    dict[value].next = dict[next_node]

  head = dict[0]

  print(find_loop(head))