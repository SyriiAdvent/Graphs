from util import Stack, Queue  # These may come in handy

def earliest_ancestor(ancestors, starting_node):
    print(f"find node: {starting_node}")

    queue = Queue()
    current = starting_node
    cache = {}
    for ancestor in ancestors: 
        parent = ancestor[0]
        child = ancestor[1]
        if child not in  cache:
            cache[child] = parent
    if starting_node not in cache:
        return -1
    print(cache)
    has_parent = True
    temp = cache[starting_node]
    temp2 = None
    while has_parent:
        if cache.get(temp) is not None:
            temp = cache.get(temp)
        else:
            has_parent = False
    return temp


    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
     (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 3))