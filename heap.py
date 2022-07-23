from hashlib import new
from heapq import merge
from operator import index
from typing import Any


class MaxHeap:
    def __init__(self, heapsize):
        """
        Initialize new MaxHeap object.
        """
        #  do i need it ?
        # zself.root
        self.priority = None
        self.heapsize = heapsize
        # i have crerated limited size and it made some problems
        # making maxsize will work better
        self.heap = [0]*( heapsize +1 )
        self.heap[0] = 0
        self.curnode = 1


    @staticmethod
    def parent(i: int) -> int:
        """
            This method is static.
            Takes an index and returns the index of the parent of this index.
            :param i: int
        """
        # // used for floor of this to get the parent
        return i//2
        

    @staticmethod
    def left_child(i: int) -> int:
        """
            This method is static.
            Takes an index and returns the index of the left child of this index.
            :param i: int
        """
        return 2*i

    @staticmethod
    def right_child(i: int) -> int:
        """
            This method is static.
            Takes an index and returns the index of the left child of this index.
            :param i: int
        """
        return 2*i+1

    def isLeaf(self, pos):
        if pos >= (self.heapsize//2) and pos <= self.heapsize:
            return True
        return False

    def size(self) -> int:
        """
        Returns the max-heap size.
        """
        return self.curnode

    def bubble_up(self, i: int) -> None:
        """
        Take an index and bubble up this index.
        :param index: int
        """

        if self.heap[i//2]>self.heap[i]:
            child = self.heap[i]
            parent = self.heap[i//2]
            child,parent = parent,child
            i=i//2
            self.bubble_up(i)
            print(self.heap[i//2])
        else:
            return

    def bubble_down(self, i: int) -> None:
        """
            Take an index and bubble down this index.
            :param index: int
        """
        # in bubbling down we might face that our two child may have problems
        # so we have to swap the smaller if we are doing max_heap
        if not self.isLeaf(i):
            if self.heap[MaxHeap.right_child(i)]>self.heap[MaxHeap.left_child(i)]:
                # swap with the right
                self.heap[MaxHeap.right_child(i)],self.heap[i] =self.heap[i],self.heap[MaxHeap.right_child(i)]
                i = self.right_child(i)
                self.bubble_down(i)
            else:
                # swap with the left with the root
                self.heap[MaxHeap.left_child(i)],self.heap[i] =self.heap[i],self.heap[MaxHeap.left_child(i)]
                i =self.left_child(i)
                self.bubble_down(i)
  
        # if there is nothing left,the process will terminate
 
    def insert(self, item: Any) -> None:
        """
        Insert new item in max-heap.
        :param item:
        """

        if self.curnode > self.heapsize :
            print("error adding more to the heap")
        else:
            self.heap[self.curnode]=item
            self.bubble_up(self.curnode)
            self.curnode += 1

            

            
    def extract_max(self) -> Any:
        """
        Return max element of the heap and remove it.
        """
        maximum = self.heap[1]
        self.heap[1]=self.heap[-2]
        # MaxHeap.build_heap_with_bubble_down(self.heap)
        return maximum 

    def find_max(self) -> Any:
        """
        Just return max element of the heap.
        """
        return self.heap[0]    

    @staticmethod
    def build_heap_with_bubble_down(arr: list) -> None:
        """
            This method is static.
            Take a list and create a max heap with this elements by bubble-down operation.
        """
        #i shouldent use the self.heap item here as it is not built for
        #this purpose
        #we start from the top
        
        # MaxHeap.bubble_down()
        
        
       
        pass
        
    def clear(self) -> None:
        """
        Clear max-heap.
        """
        self.heap.clear()

    @staticmethod
    def merge(mh1, mh2):
        """
        This method is static.
        Takes 2 objects of MaxHeap, merge theirs and returns new MaxHeap object.
        :param mh1: MaxHeap object.
        :param mh2: MaxHeap object.
        :return: MaxHeap object.
        """
        # we will create anothe maxheap with the least space complexity
        # we have another way that is expanding one of the maxheaps and and delete the old items
        newheap = MaxHeap(mh1.size() + mh2.size())
        # is it OK????? i need to check if it needs to assign newheap to it again
        newheap.insert(mh1.heap)
        for i in range(mh1.size()):
            newheap.heap[i] =mh1.heap[i]
        # i couldent use one loop as i need to append to the last
        for j in range(mh1.size(),mh1.size() + mh2.size()):
            newheap.heap[j] =mh2.heap[j-mh1.size()]
            #  i have problem in this believe me
        newheap = MaxHeap.build_heap_with_bubble_up(newheap.heap)

        return newheap
        

    def add_to_all(self, delta: Any) -> None:
        """
        Add delta to each elements in the max-heap.
 
        """
                          # heap.size()
        for i in range(len(self.heap)):
            #add items to the array we use
            self.heap[i]+=int(delta)

    def display(self):
        print(self.heap)
        # this way of showing is very bad i need to check it if right

def test(getans,desiredans):
    if getans ==desiredans:
        print("passed") 
    print("your answer is : ",getans)
    print("the desired answer is : ",desiredans)

sample = MaxHeap(7)

sample.insert(1)
print(MaxHeap.right_child(sample.curnode))
sample.insert(2)
print(MaxHeap.right_child(sample.curnode))
sample.insert(3)
print(MaxHeap.right_child(sample.curnode))
sample.insert(4)
print(MaxHeap.right_child(sample.curnode))
sample.insert(5)
print(MaxHeap.right_child(sample.curnode))
sample.insert(18)
print(MaxHeap.right_child(sample.curnode))
sample.insert(122)
print(MaxHeap.right_child(sample.curnode))
sample.display()
print(MaxHeap.right_child(sample.curnode))






