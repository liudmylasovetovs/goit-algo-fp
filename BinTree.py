import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs_traversal(node, visited, colors):
    if node is None:
        return colors
    visited.add(node)
    for neighbor in [node.left, node.right]:
        if neighbor and neighbor not in visited:
            colors[neighbor.id] = next_color(colors[node.id])
            dfs_traversal(neighbor, visited, colors)
    return colors


def bfs_traversal(root):
    visited = set()
    queue = [root]
    visited.add(root)
    colors = {root.id: '#1296F0'}  # Початковий колір
    while queue:
        current = queue.pop(0)
        for neighbor in [current.left, current.right]:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                colors[neighbor.id] = next_color(colors[current.id])
    return colors


def next_color(prev_color):
    # Функція, що генерує наступний колір на основі попереднього
    r, g, b = hex_to_rgb(prev_color)
    r = min(255, int(r * 1.2))  # Збільшення червоного складника кольору
    g = min(255, int(g * 1.2))  # Збільшення зеленого складника кольору
    b = min(255, int(b * 1.2))  # Збільшення синього складника кольору
    return rgb_to_hex(r, g, b)


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    if traversal_type == 'DFS':
        colors = dfs_traversal(tree_root, set(), {tree_root.id: '#1296F0'})
    elif traversal_type == 'BFS':
        colors = bfs_traversal(tree_root)
    else:
        raise ValueError("Invalid traversal type. Choose 'DFS' or 'BFS'.")

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(colors.values()))
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом у глибину
draw_tree(root, 'DFS')

# Відображення дерева з обходом у ширину
draw_tree(root, 'BFS')



