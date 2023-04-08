"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node : return None
        d = dict()
        def compute(node):
            if node.val in d:
                return d[node.val]
            copyNode = Node(node.val)
            d[node.val]=copyNode
            for nxt in node.neighbors:
                r = compute(nxt)
                copyNode.neighbors.append(r)
            
            return copyNode
        return compute(node)