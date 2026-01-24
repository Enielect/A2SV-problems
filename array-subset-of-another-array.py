class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        #code here
        map_a, map_b = {}, {}
        
        for num in a:
            map_a[num] = map_a.get(num, 0) + 1
        
        for num in b:
            map_b[num] = map_b.get(num, 0) + 1
        
        for key in map_b:
            if key not in map_a or map_b[key] > map_a[key]: return False
        return True
