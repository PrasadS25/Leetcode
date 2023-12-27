import math
import sys
class KthLargest:

    def __init__(self, k: int, nums):
        self.size = 0
        self.maxsize = k
        self.min_heap = []
        if len(nums)>0:
            for i in nums:
                self.add(i)
        
    def heapify(self,pos:int):
        
        parent = (pos-1)//2
        if pos==0:
            return
        if parent>=0 and self.min_heap[parent]>self.min_heap[pos]:
            self.min_heap[parent],self.min_heap[pos] = self.min_heap[pos],self.min_heap[parent]
            self.heapify(parent)


        # parent = (pos - 1) // 2
        # while pos > 0 and self.min_heap[parent] > self.min_heap[pos]:
        #     self.min_heap[parent], self.min_heap[pos] = self.min_heap[pos], self.min_heap[parent]
        #     pos = parent
        #     parent = (pos - 1) // 2


    def delete(self,pos):
        l=2*pos+1
        r=2*pos+2
        least = pos
        
        
        if l<self.size and self.min_heap[l]<self.min_heap[least]:
            least = l
        if r<self.size and self.min_heap[r]<self.min_heap[least]:
            least = r
        
        if least != pos:
            self.min_heap[pos],self.min_heap[least] = self.min_heap[least],self.min_heap[pos]
            self.delete(least)
        
        
        
        
    def add(self, val: int) -> int:
        if self.size<self.maxsize:
            
            self.min_heap.append(val)
            self.heapify(self.size)
            self.size+=1
        elif val>self.min_heap[0]:
            self.min_heap.append(val)
            self.heapify(self.size)
            self.size+=1
            
            # self.min_heap[0] = self.min_heap.pop()
            # self.size-=1
            
            self.size -= 1
            self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
            self.min_heap.pop()

            self.delete(0)
            
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)