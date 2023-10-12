# s05
# 👉  discussion
#    👉 linklist.py

# [6][3][4][2][1]

#     head -> [6]--,      ,----->[4]---,
#                     |          |                 '-->[2]
#  ,->[1]          '->[3]----'                      |
#  |                                                      |
#   '-----------------------------------------------'

# head.data = 6
# head.next.data = 3
# head.next.next
# head.next.next.next.data = 2

# Singularly linked list
#  ,----->[6]•‐--->[3]•---->[4]•---->[2]•---->[1]•----,
#  |                                                                        |
#   '--------------------------------------------------------------'
# circular linked list

# Initialization
class Box {
    int data
    Box next
}

# Construction
class Node {
    int data
    Node next
    Node(int data){
        this.data = data
    }
}

Create node(5)
Node NodeA = new Node(6)
Node NodeB = new Node(3)
Node NodeC = new Node(4)
Node NodeD = new Node(2)
Node NodeE = new Node(1)

NodeA.next = NodeB
NodeB.next = NodeC
NodeC.next = NodeD
NodeD.next = NodeE
NodeE.next = null

# If this was an array...
# f[0] = pointer
# instead it's...
# head --> (6)
# head.data = 6

