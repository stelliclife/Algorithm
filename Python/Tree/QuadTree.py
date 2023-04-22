class Node:
    def __init__(self, value, is_leaf=True):
        self._value = value
        self._is_leaf = is_leaf
        self._north_west = None
        self._north_east = None
        self._south_west = None
        self._south_east = None

    @property
    def value(self):
        return self._value

    @property
    def is_leaf(self):
        return self._is_leaf

    @property
    def north_west(self):
        return self._north_west

    @north_west.setter
    def north_west(self, node):
        self._north_west = node

    @property
    def north_east(self):
        return self._north_east

    @north_east.setter
    def north_east(self, node):
        self._north_east = node

    @property
    def south_west(self):
        return self._south_west

    @south_west.setter
    def south_west(self, node):
        self._south_west = node

    @property
    def south_east(self):
        return self._south_east

    @south_east.setter
    def south_east(self, node):
        self._south_east = node

def quad_tree(grid):
    def subtree(s, e, length, node):
        container = []
        if length == 1:
            return container

        k = length // 2

        node.north_west = Node(grid[s][e])
        node.north_east = Node(grid[s][e+k])
        node.south_west = Node(grid[s+k][e])
        node.south_east = Node(grid[s+k][e+k])
        if node.north_west.value == node.north_east.value == node.south_west.value == node.south_east.value:
            container.append(node.north_west.value)
            return container
        else:
            if length == 2:
                temp = [node.north_west.value, node.north_east.value, node.south_west.value, node.south_east.value]
                container.extend(temp)
        output = subtree(s, e, k, node.north_west)
        container.extend(output)
        output = subtree(s, e+k, k, node.north_east)
        container.extend(output)
        output = subtree(s+k, e, k, node.south_west)
        container.extend(output)
        output = subtree(s+k, e+k, k, node.south_east)
        container.extend(output)
        return [container]

    size = len(grid)
    half = size // 2
    root = Node(1)
    if grid[0][0] == grid[0][half] == grid[half][0] == grid[half][half]:
        root = Node(grid[0][0])
        return [root.value]

    result = subtree(0, 0, size, root)
    return result

if __name__ == '__main__':
    table = [[1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 0, 0, 1, 1]]
    print(quad_tree(table))