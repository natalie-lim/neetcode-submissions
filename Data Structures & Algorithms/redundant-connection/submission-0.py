class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parent is the root of the set that i belongs to
        parent = list(range(len(edges) + 1))

        def find(x):
            # walk up parent chain until hit node that's its own parent
            while parent[x] != x: # x is not a root keep calling
                # path compression?
                parent[x] = parent[parent[x]] # flatten tree up
                x = parent[x]

            return x
        
        for u, v in edges:
            ru, rv = find(u), find(v) # find root of each

            if ru == rv:
                return [u, v]

            # otherwise, u and v are in diff components, merge them by making one point to the other
            parent[ru] = rv
