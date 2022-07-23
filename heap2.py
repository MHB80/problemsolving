import math
class MaxHap:
    def __init__(self,maxsize) -> None:    
        self.heap = []  
        self.heap.append(0)
        self.maxsize =maxsize+1
        self.currentnode = 1

    def insert(self,item):
        if self.currentnode > self.maxsize:
            print("no")
        else:
            self.heap.append(item)
            print(self.heap[-1])  
            if  self.heap[-1]>self.heap[1]:
                self.bubble_up(self.currentnode)
            self.currentnode +=1
    def delete(self):
        if self.currentnode > 1 :
            self.heap.pop()
            self.currentnode -=1
            
            self.bubble_down(1)
        else:
            print("tree is empty")
    @staticmethod
    def swap(list,pos1,pos2):
        list[pos1],list[pos2] = list[pos2],list[pos1]
        return list
    def isleaf(self,i):
        if 2*i >self.currentnode and i>self.currentnode:
            return False
        else:
            return True
    def parent(self,i:int):
            return i//2
    def rchild(self,i):
        return 2*i+1
    def lchild(self,i):
        return 2*i
    def bubble_up(self,i):
        if self.parent(i)>=1 :
                # print(self.heap[self.parent(i)],self.heap[i])
                while(i!=0):
                    self.heap=self.swap(self.heap,i,self.parent(i))
                    i = i//2
                    self.bubble_up(i)

        else:
            pass
        
    def bubble_down(self,i):
                if not self.isLeaf(i):
                    if self.heap[self.rchild(i)]>self.heap[self.lchild(i)]:
                        # swap with the right
                        self.heap[self.rchild(i)],self.heap[i] =self.heap[i],self.heap[self.rchild(i)]
                        i = self.right_child(i)
                        self.bubble_down(i)
                    else:
                # swap with the left with the root
                        self.heap[self.lchild(i)],self.heap[i] =self.heap[i],self.heap[self.lchild(i)]
                        i =self.left_child(i)
                        self.bubble_down(i)
    def displaymax(self):
        maxitem = self.heap[1]
    def exctractmax(self):
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.bubble_down()
    def display(self):
        print(self.heap)
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
        newheap = MaxHap(mh1.size() + mh2.size())
        # is it OK????? i need to check if it needs to assign newheap to it again
        newheap.insert(mh1.heap)
        for i in range(mh1.size()):
            newheap.heap[i] =mh1.heap[i]
        # i couldent use one loop as i need to append to the last
        for j in range(mh1.size(),mh1.size() + mh2.size()):
            newheap.heap[j] =mh2.heap[j-mh1.size()]
            #  i have problem in this believe me
        newheap = MaxHap.build_heap_with_bubble_up(newheap.heap)

        return newheap
sample = MaxHap(7)
sample.insert(8)
sample.insert(4)
sample.insert(5)
sample.insert(7)
sample.insert(4)
sample.insert(5)
sample.display()

