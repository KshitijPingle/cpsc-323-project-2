# Class to make a list of tree nodes

class tree_node:
    def __init__(self, element):
        self.element = element
        # Initialize a list of children for this node
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    # Func has spaces argument for it to be recursive
    def print_tree(self, spaces = "", last_node = True):
        if (last_node):
            connection = "└── "
        else:
            connection = "├── "

        line = spaces + connection + self.element
        print(line)

        if (last_node):
            spaces += "    "
        else:
            spaces += "│   "
        
        # Now call recursively to print all subtrees
        counter = 0
        for child_node in self.children:
            # Check if child node is last node
            if (counter >= (len(self.children) - 1)):
                last_node = True
            else:
                last_node = False

            child_node.print_tree(spaces, last_node)
            counter += 1