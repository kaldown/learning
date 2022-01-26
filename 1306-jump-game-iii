class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        
        def get_next_pair(val):
            return val + arr[val], val - arr[val]
        
        q = [start]
        visited = set()
        while q:
            val = q.pop()
            
            if val >= len(arr):
                visited.add(val)
            
            if val in visited:
                continue

            val1, val2 = get_next_pair(val)
            
            if 0 <= val1 < len(arr):
                q.append(val1)
                if arr[val1] == 0:
                    return True

            if 0 <= val2 < len(arr):
                q.append(val2)
                if arr[val2] == 0:
                    return True
            
            visited.add(val)
            
        return False
        
