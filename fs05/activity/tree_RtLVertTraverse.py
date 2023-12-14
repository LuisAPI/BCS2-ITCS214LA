# De La Salle University–Dasmariñas
# S-ITCS214LA — Data Structures & Algorithms (Laboratory)

# Luis Anton P. Imperial
# BCS22

# Thursday, December 14, 2023
# 231211 — Final Laboratory Examination

# Create an algorithm that find the vertical traversal of  Binary tree, starting from the rightmost to the leftmost level. If there are multiple nodes passing through a vertical line then they should be printed as they appear in level order traversal of the tree.

'''
Output:

        9  7   8   3   6   5   1   2   4

        Vertical Order traversal is: 
  A - 4

  B - 2

  C - 1 5 6

  D - 3 8

  E - 7

  F - 9

Your task is to read the input and print the vertical traversal based on your algorithm, which it takes the root node as input parameter and returns an array containing the vertical order traversal of the tree from the leftmost to the rightmost level. If 2 nodes lie in the same vertical, they should printed in order they appear in the level order traversal of the tree

 

Expected Time Complexity : O(n*log(n))

Expected Space Complexity : O(n)
'''

class Node:
    def __init__(self, node_value):
        self.data = node_value
        self.left = None
        self.right = None
    
def traverseLtR(root_node, distance, tree):
    if root_node is None:
        return []

    queue = [(root_node, 0)]

    while queue:
        # Define node and distance from the user-assigned root node
        node, distance = queue.pop(0)

        if distance in tree:
            # Add the node next to node with said index
            tree[distance].append(node.data)
        else:
            # If tree as indexed by distance doesn't have a value, add the proposed data to that part of the tree
            tree[distance] = [node.data]
        
        if node.left:
            queue.append((node.left, distance - 1))
        
        if node.right:
            queue.append((node.right, distance + 1))
    
    sorted_tree = sorted(tree.items())

    sorted_tree_pouredOver = []
    for distance, nodes in sorted_tree:
        sorted_tree_pouredOver.extend(nodes)
    
    return sorted_tree_pouredOver

def create_treeLtR(root_node_input):
    # Create dictionary of tree nodes (and their distance away from root)
    tree_shown = {}
    distance = 0

    return traverseLtR(root_node_input, distance, tree_shown)

def show_treeLtR(root_node_input):
    print("Values of your chosen tree (left-to-right):")
    # Print each value with 3 spaces gap, like so: {source_variable:^3}
    treeLtR = create_treeLtR(root_node_input)

    for value in treeLtR:
        print(f"{value:^3}", end=" ")

    print("")

def show_treeRtL(tree_LtR):
    tree_values_LtR = create_treeLtR(tree_LtR)

    print("Values of your chosen tree (right-to-left):")
    # Print each value with 3 spaces gap, like so: {source_variable:^3}
    for value in tree_values_LtR[::-1]:
        print(f"{value:^3}", end=" ")

    print("")

def main():    
    # Inputs here
    input_root = Node(1)
    input_root.left = Node(2)
    input_root.right = Node(3)
    input_root.left.left = Node(4)
    input_root.left.right = Node(5)
    input_root.right.left = Node(6)
    input_root.right.right = Node(7)
    input_root.right.left.right = Node(8)
    input_root.right.right.right = Node(9)

    show_treeLtR(input_root)
    print()
    
    show_treeRtL(input_root)

if __name__ == "__main__":
    main()