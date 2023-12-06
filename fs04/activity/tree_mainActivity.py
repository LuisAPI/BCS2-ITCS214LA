## De La Salle University–Dasmariñas
## S-ITCS214LA — Data Structures & Algorithms (Laboratory)

## Luis Anton P. Imperial
## BCS2-2

## Tuesday, December 5, 2023
## 231204 - Main Activity

## Create a tree from python file that shows this tree structure based on Mini-activity tree figure
##  And based on this python file, identify the following:
## - root
## - Leaves
## - ancestors of H
## - descendants of G
## - siblings of I
## - parent of K
## - children of D
## - height of the tree
## - height of node G
## - level of node H
## - level of node A
## - height of node E
## - draw the subtrees of node G

from bigtree import Node

# List all elements of the tree, as a dictionary
path_dict = {
    "a": {"name": "A"},
    "a/b": {"name": "B"},
    "a/b/c": {"name": "C"},
    "a/b/d": {"name": "D"},
    "a/b/d/e": {"name": "E"},
    "a/b/d/f": {"name": "F"},
    "a/g": {"name": "G"},
    "a/g/h": {"name": "H"},
    "a/g/h/i": {"name": "I"},
    "a/g/h/j": {"name": "J"},
    "a/g/h/k": {"name": "K"},
    "a/g/h/j/l": {"name": "L"},
    "a/g/h/k/m": {"name": "M"},
}

# Create a dictionary to keep track of created nodes
created_nodes = {
    "a": Node("A", data = path_dict["a"] )
    }

# Create nodes and add them to the tree
for path, node_data in path_dict.items():
    # Skip the root node
    if path != "a":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent = current_node, data = path_dict[path])
            current_node = created_nodes[node]

# showing the tree structure with specified attributes
created_nodes["a"].show(attr_list = ["name"])

#####

# Mini-Activity Identification Answers
import yaml

subtrees_G_question = "13. Draw the subtrees of node G:"
subtrees_G = """
    G
    |
    H
   /| \\
 /  |   \\
I   J    K
    |    |
    L    M
"""

answers = {
    "01. root": "A",
    "02. leaves": "C, E, F, I, L, M",
    "03. ancestors of H": "A, G",
    "04. descendants of G": "H, I, J, K, L, M",
    "05. siblings of I": "J, K",
    "06. parent of K": "H",
    "07. children of D": "E, F",
    "08. height of the tree": 4,
    "09. height of node G": 3,
    "10. level of node H": 2,
    "11. level of node A": 0,
    "12. height of node E": 0,
}

print("")
print("Identification —")
print(yaml.dump(answers))
print(subtrees_G_question, subtrees_G)