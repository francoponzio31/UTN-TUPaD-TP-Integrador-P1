def find_path_from_root(tree, target, path=None):
    if path is None:
        path = []
    if not tree:
        return None
    node = tree[0]
    path = path + [node]
    if node == target:
        return path
    for child in tree[1:]:
        if child:
            res = find_path_from_root(child, target, path)
            if res:
                return res
    return None

def find_path_between(tree, start, end):
    path_to_start = find_path_from_root(tree, start)
    path_to_end = find_path_from_root(tree, end)
    if not path_to_start or not path_to_end:
        print("No path found.")
        return
    # Encuentra el ancestro común más cercano
    i = 0
    while i < min(len(path_to_start), len(path_to_end)) and path_to_start[i] == path_to_end[i]:
        i += 1
    # Camino: subir de start a ancestro común, luego bajar a end
    path = path_to_start[:i-1:-1] + path_to_end[i-1:]
    print(" -> ".join(path))

def find_node(tree, value, level=0):
    if not tree:
        return None, -1
    if tree[0] == value:
        return tree, level
    for child in tree[1:]:
        if child:
            res, lvl = find_node(child, value, level+1)
            if res:
                return res, lvl
    return None, -1

def degree(node):
    if not node:
        return 0
    return sum(1 for child in node[1:] if child)

def is_root(tree, value):
    return tree[0] == value

def is_leaf(node):
    for child in node[1:]:
        if child:
            return False
    return True

def is_branch(tree, node, value):
    return not is_root(tree, value) and not is_leaf(node)

def depth(node, value, level=0):
    if not node:
        return -1
    if node[0] == value:
        return level
    for child in node[1:]:
        if child:
            prof = depth(child, value, level+1)
            if prof != -1:
                return prof
    return -1
