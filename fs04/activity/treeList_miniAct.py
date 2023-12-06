## De La Salle University–Dasmariñas
## S-ITCS214LA — Data Structures & Algorithms (Laboratory)

## Luis Anton P. Imperial
## BCS2-2

## Tuesday, December 5, 2023
## Bigtree: Mini-Activity
##        - create a new node as children of b with a value of 'Jungkook'
##        - add children to c with a value of 'Suga'
##        - from Suga add children of node Jimin
##
##              -- using dictionary to tree
##    Screen shot the your code and result in our SB Laboratory

'''
    bigtree python package can construct tree and export tree
        - big tree setup
            -- pip install bigtree
        - to export image
            -- pip install 'bigtree[image]'
        - to update pip
            -- pip install --upgrade pip
'''
# from bigtree import Node

# a = Node("root", data = "RM")
# b = Node("a", data = "Jin", parent = a)
# c = Node("b", data = "Jhope", parent = a)
# d = Node("c", data = "V", parent = b)
# e = Node("d", data = "Jungkook", parent = b)
# f = Node("e", data = "Suga", parent = c)
# g = Node("f", data = "Jimin", parent = f)

# print(a.children)

# #depth
# print(f.depth)

# a.show(attr_list = ["data"])


#pip install 'bigtree[pandas]'
from bigtree import Node, list_to_tree

## a = Node("root", value = "RM")
## b = Node("a", value = "Jin")
## c = Node("b", value = "Jhope")
## d = Node("c", value = "V")
## e = Node("d", value = "Jungkook")
## f = Node("e", value = "Suga")
## g = Node("f", value = "Jimin")

path_list = ["a/b/d", "a/b/e", "a/c"]

root = list_to_tree(path_list)

root.show()
## def display_node_data(node):
##     print(node.value)


## def traverse_and_display(node):
##     display_node_data(node)
##     for child in node.children:
##         traverse_and_display(child)

## traverse_and_display(root)
## root.show(attr_list = ["data"])
print("-------------------------------------")
#dictionary to tree
from bigtree import Node

path_dict = {
    "a": {"name": "RM"},
    "a/b": {"name": "Jin"},
    "a/c": {"name": "Jhope"},
    "a/b/d": {"name": "Jungkook"},
    "a/b/e": {"name": "V"},
    "a/c/f": {"name": "Suga"},
    "a/c/f/g": {"name": "Jimin"}
}

#Create a dictionary to keep track of created nodes
created_nodes = {"a": Node("RM", data = path_dict["a"] )}

#Create nodes and add them to the tree
for path, node_data in path_dict.items():
    #skip the root node
    if path != "a":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent = current_node, data = path_dict[path])
            current_node = created_nodes[node]

#showing the tree structure with specified attributes
created_nodes["a"].show(attr_list = ["name"])