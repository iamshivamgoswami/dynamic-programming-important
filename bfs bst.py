import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        level=[]
        nodes=collections.deque([root,None])
        if not root:
            return []
        while len(nodes)>0:
            curr_node=nodes.popleft()
            if curr_node:
                level.append(curr_node.val)
                if curr_node.left:
                    nodes.append(curr_node.left)
                if curr_node.right:
                    nodes.append(curr_node.right)

            else:
                res.append(level)
                if len(nodes)>0:
                    nodes.append(None)
                level=[]
        return res


