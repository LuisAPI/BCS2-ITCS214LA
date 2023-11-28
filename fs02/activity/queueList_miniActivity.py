# De La Salle University–Dasmariñas

# Luis Anton P. Imperial
# BCS22
# Tuesday, November 28, 2023

# S-ITCS214LA — Circular Queue
# Mini-Activity: Add a `dequeue()` function to the Queue class.

'''
    FIFO

    Operation of Queue
        - enqueue() - to insert
            Steps:
                - check the queue is full or not
                - if full --- 'overflow'
                - if not full
                    - increment the tail
                    - add the element
        - dequeue() - to remove
        - front()
        - rear()
        - isEmpty()
        - isFull
        - size()
'''

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.QList[self.rear] = item
        self.size = self.size + 1
        print("%s add to list " % str(item))

    def dequeue(self):
        if self.isEmpty():
            print("Error! — Empty list.")
            return
        
        # Should be above the actual dequeueing process, else this produces the new front item.
        print("%s removed from list." % str(self.QList[self.front]))

        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def queueFront(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Front item is ", self.QList[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Rear item is ", self.QList[self.rear])
    
    def printBothEnds(self):
        self.queueFront()
        self.queueRear()

if __name__ == '__main__':
    queue = Queue(5)

    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(25)
    queue.enqueue(1)
    queue.enqueue(250)
    print("")

    queue.queueFront()
    queue.queueRear()
    print("")

    queue.dequeue()
    queue.dequeue()
    print("")

    queue.printBothEnds()
    print("")

    queue.dequeue()
    print("")

    queue.printBothEnds()

'''
    Mini-Activity = 10 mins
    Create dequeue function on this code

    Screenshot the code and the result
'''