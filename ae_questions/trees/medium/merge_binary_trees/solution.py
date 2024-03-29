"""
Given 2 binary trees, merge them and return the result. If there are nodes at the same relative position in both trees, sum them.

NOTE: TC analyses in the comments above the respective merge functions
"""
import sys
from os import path

sys.path.append(path.dirname( path.dirname ( path.dirname ( path.abspath(__file__) ) ) ))

from ae_bst import Tree as t

# node class, to create new nodes with each invocation of merge()
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

"""
* ORIGINAL SOLUTION *
merges values of node1 and node2.

TC: O(n) -- where n = number of nodes in the larger tree
SC: O(d + n) -- where d1 = depth of larger tree and n = nodes in the new tree
"""
def merge1(node1, node2):
  if not node1 and not node2:
    return None

  n1_val, n2_val = 0 if not node1 else node1.value, 0 if not node2 else node2.value
  combined = Node(n1_val + n2_val)

  n1_left, n2_left = None if not node1 else node1.left, None if not node2 else node2.left
  n1_right, n2_right = None if not node1 else node1.right, None if not node2 else node2.right

  combined.left, combined.right = merge1(n1_left, n2_left), merge1(n1_right, n2_right)

  return combined


"""
* SOLUTION 2 *
merges values of node1 and node2.

! Optimizations over Solution 1:
  - less space used, as the original tree1 is modified in-place
  - if nothing found at a given node for either tree, just return the other tree
    - this means you can just traverse down until the shorter tree ends at any given node

TC: O(n) -- where n is the number of nodes in the smaller tree (don't need to traverse through the larger tree at any given node at any point in either tree)
SC: O(d) -- where d is the max depth in the smaller tree at any given point
"""
def merge2(node1, node2):
  if not node1: return node2
  if not node2: return node1
  node1.value = node1.value + node2.value
  node1.left, node1.right = merge2(node1.left, node2.left), merge2(node1.right, node2.right)
  return node1


def merge_binary_trees(tree1, tree2):
  # return merge1(tree1, tree2)
  return merge2(tree1, tree2)


if __name__ == "__main__":
  t1, t2 = t(), t()

  nodes1 = [
    {"id": "1", "left": "3", "right": "2", "value": 1},
    {"id": "3", "left": "5", "right": None, "value": 3},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "2", "left": None, "right": None, "value": 2}
  ]

  nodes2 = [
    {"id": "2", "left": "3", "right": "6", "value": 2},
    {"id": "3", "left": None, "right": "4", "value": 3},
    {"id": "6", "left": None, "right": "7", "value": 6},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "7", "left": None, "right": None, "value": 7}
  ]

  for node in nodes1: t1.insert_node(t1.root, node)
  for node in nodes2: t2.insert_node(t2.root, node)

  print('t1:', t1.preorder_traversal(t1.root, list=[]))
  print('t2:', t2.preorder_traversal(t2.root, list=[]))

  print(merge_binary_trees(t1.root, t2.root))