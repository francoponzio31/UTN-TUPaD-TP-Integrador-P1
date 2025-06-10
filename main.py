from node_utils import find_path_between, find_node, degree, is_root, is_leaf, is_branch
from print_utils import preorder, postorder, inorder, tree_structure, clear_screen
from tree import tree
import time


def menu():
    clear_screen()
    print("1. Find path between nodes")
    print("2. Print tree (preorder, postorder, inorder, structure)")
    print("3. Node details (depth, level, degree, is root, is branch, is leaf, childrens)")
    print("4. Exit")
    return input("Select an option: ")

if __name__ == "__main__":

    while True:
        option = menu()
        if option == "1":
            clear_screen()
            start = input("Start node: ").strip().upper()
            end = input("End node: ").strip().upper()
            print("Found paths:")
            find_path_between(tree, start, end)
            input("Press Enter to continue...")
        elif option == "2":
            clear_screen()
            print("Preorder:")
            preorder(tree)
            print()
            print("Postorder:")
            postorder(tree)
            print()
            print("Inorder:")
            inorder(tree)
            print()
            print("Tree structure:")
            tree_structure(tree)
            input("Press Enter to continue...")
        elif option == "3":
            clear_screen()
            value = input("Enter node: ").strip().upper()
            node, level = find_node(tree, value)
            if node:
                print(f"Depth: {level}")
                print(f"Level: {level+1}")
                print(f"Degree: {degree(node)}")
                print(f"Is root: {is_root(tree, value)}")
                print(f"Is branch: {is_branch(tree, node, value)}")
                print(f"Is leaf: {is_leaf(node)}")
                print(f"Children nodes: {', '.join(child[0] for child in node[1:] if child) or 'None'}")
                input("Press Enter to continue...")
            else:
                print("Node not found.")
                input("Press Enter to continue...")
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")
            time.sleep(1)