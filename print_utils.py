def preorder(tree):
    if tree:
        print(tree[0], end=" ")
        preorder(tree[1])
        preorder(tree[2])

def postorder(tree):
    if tree:
        postorder(tree[1])
        postorder(tree[2])
        print(tree[0], end=" ")

def inorder(tree):
    if tree:
        inorder(tree[1])
        print(tree[0], end=" ")
        inorder(tree[2])


def tree_structure(tree, nivel=0):
    if tree:
        tree_structure(tree[2], nivel + 1)
        print("     " * nivel + str(tree[0]))
        tree_structure(tree[1], nivel + 1)


def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")