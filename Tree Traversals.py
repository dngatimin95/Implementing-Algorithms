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


# level order traversal - recursive (DFS)



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
