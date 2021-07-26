import collections


def findDist(root, a, b):
    ans = None

    def lca(node, a, b):
        nonlocal ans
        if not node:
            return False
        left = lca(node.left, a, b)
        right = lca(node.right, a, b)
        mid = node.data == a or node.data == b
        if mid + left + right >= 2:
            ans = node
        return mid or left or right

    lca(root, a, b)

    aa, bb = None, None
    l = None

    def bfs(node):
        nonlocal l, aa, bb

        res = []

        n = 0
        nodes = collections.deque([root, None])
        while nodes:
            curr_element = nodes.popleft()

            if curr_element:

                if curr_element == ans:
                    l = n
                if curr_element.data == a:
                    aa = n
                if curr_element.data == b:
                    bb = n
                if curr_element.left:
                    nodes.append(curr_element.left)
                if curr_element.right:
                    nodes.append(curr_element.right)
            else:
                n += 1
                if nodes:
                    nodes.append(None)

    bfs(root)

    return (aa - l) + (bb - l)