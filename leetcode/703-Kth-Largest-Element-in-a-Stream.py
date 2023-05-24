from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._right = sorted(nums)[-self._k:]

    def push(self, val):
        heappush(self._right, val)
 
    def pop(self):
        return heappop(self._right)

    @property
    def kth(self):
        kth = self.pop()
        self.push(kth)
        return kth
        
    def add(self, val: int) -> int:
        if len(self._right) >= self._k:
            if val <= self.kth:
                return self.kth
            self.pop()
            self.push(val)
            return self.kth
        else:
            self.push(val)
            return self.kth


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
