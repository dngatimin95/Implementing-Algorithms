# inorder traversal - recursive
def inorder(root):
    stack = []
    traverse_inorder(root,stack)
    return stack

def traverse_inorder(root, stack):
    if root:
        traverse_inorder(root.left, stack)
        stack.append(root.val)
        traverse_inorder(root.right, stack)

# inorder traversal - iterative
def inorder_iterative(root):
    stack, inorder = [], []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        inorder.append(root.val)
        root = root.right
    return inorder

# preorder traversal - recursive
def preorder(root):
    stack = []
    traverse_preorder(root,stack)
    return stack

def traverse_preorder(root, stack):
    if root:
        stack.append(root.val)
        traverse_preorder(root.left, stack)
        traverse_preorder(root.right, stack)

# preorder traversal - iterative
def preorder_iterative(root):
    stack, preorder = [root], []
    while stack:
        node = stack.pop()
        if node:
            preorder.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return preorder


# postorder traversal - recursive
def postorder(root):
    stack = []
    traverse_postorder(root,stack)
    return stack

def traverse_postorder(root, stack):
    if root:
        traverse_postorder(root.left, stack)
        traverse_postorder(root.right, stack)
        stack.append(root.val)

# postorder traversal - iterative
def postorder_iterative(root):
    stack, postorder = [root], []
    while stack:
        node = stack.pop()
        if node:
            postorder.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return postorder[::-1]

# level order traversal - recursive (DFS)
def levelOrder(root):
    res = []
    dfs(root, 0, res)
    return res

def dfs(root, level, res):
    if not root:
        return
    if len(res) < level + 1:
        res.append([])
    res[level].append(root.val)
    dfs(root.left, level+1, res)
    dfs(root.right, level+1, res)

# level order traversal - iterative (BFS)
def bfs(root):
    if root is None:
        return

    queue = []
    element = []

    queue.append(root)
    while queue:
        root = queue.pop(0)
        element.append(root.val)
        if root.left: queue.append(root.left)
        if root.right: queue.append(root.right)
    return element

# implement BST, Red bLack tree, heap
