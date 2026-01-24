class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        map_a, map_b = {}, {}
        
        for num in a:
            map_a[num] = map_a.get(num, 0) + 1
        
        for num in b:
            map_b[num] = map_b.get(num, 0) + 1
        
        for key in map_a:
            if key not in map_b or map_a[key] != map_b[key]: return False
        return True
