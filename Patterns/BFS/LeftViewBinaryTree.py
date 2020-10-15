from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def leftView(root):
  result = []
  if root is None:
    return result
  # Initialize
  queue = deque()
  queue.append(root)
  while queue:
    k = len(queue) # VERY IMPORTANT ( Recall STEP 3), This many nodes will be at current level
    for i in range(k): # process first k nodes
      currentNode = queue.popleft()
      if i == 0:
          result.append(currentNode.val)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
  return result

def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.right.left = TreeNode(7)
  print("Left View of Binary Tree: " + str(leftView(root)))
main()