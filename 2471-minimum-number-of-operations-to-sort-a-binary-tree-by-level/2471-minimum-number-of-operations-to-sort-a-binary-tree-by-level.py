# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        def minSwaps(arr):
            n = len(arr)

            # Create two arrays and use
            # as pairs where first array
            # is element and second array
            # is position of first element
            arrpos = [*enumerate(arr)]

            # Sort the array by array element
            # values to get right position of
            # every element as the elements
            # of second array.
            arrpos.sort(key = lambda it : it[1])

            # To keep track of visited elements.
            # Initialize all elements as not
            # visited or false.
            vis = {k : False for k in range(n)}

            # Initialize result
            ans = 0
            for i in range(n):

                # already swapped or
                # already present at
                # correct position
                if vis[i] or arrpos[i][0] == i:
                    continue

                # find number of nodes
                # in this cycle and
                # add it to ans
                cycle_size = 0
                j = i

                while not vis[j]:

                    # mark node as visited
                    vis[j] = True

                    # move to next node
                    j = arrpos[j][0]
                    cycle_size += 1

                # update answer by adding
                # current cycle
                if cycle_size > 0:
                    ans += (cycle_size - 1)

            # return answer
            return ans
        def compute(root,level):
            if root==None:
                return
            d[level].append(root.val)
            compute(root.left,level+1)
            compute(root.right,level+1)
        compute(root,0)
        res = 0
        for v in d:
            arr = d[v]
            res+=minSwaps(arr)
        return res;