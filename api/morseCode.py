class Node:
    def __init__(self, data, left=None, right =None):
        self.data = data
        self.left = left
        self.right = right


def encode(node,char,code):
    if node==None:
        return False
    elif node.data==char:
        return True
    else:
        if encode(node.left,char,code)==True:
            code.insert(0,".")
            return True
        elif encode(node.right, char, code)==True:
            code.insert(0,"-")
            return True
            

tree = Node("Tree")
tree.left = Node("E")
tree.right = Node("T")

tree.left.left = Node("I")
tree.left.right = Node("A")
tree.right.left = Node("N")
tree.right.right = Node("M")

tree.left.left.left = Node("S")
tree.left.left.right = Node("U")
tree.left.right.left = Node("R")
tree.left.right.right = Node("W")

tree.right.left.left = Node("D")
tree.right.left.right = Node("K")
tree.right.right.left = Node("G")
tree.right.right.right = Node("O")

tree.left.left.left.left = Node("H")
tree.left.left.left.right = Node("V")
tree.left.left.right.left = Node("F")
tree.left.left.right.right = Node("")
tree.left.right.left.left = Node("L")
tree.left.right.left.right = Node("")
tree.left.right.right.left = Node("P")
tree.left.right.right.right = Node("J")

tree.right.left.left.left = Node("B")
tree.right.left.left.right = Node("X")
tree.right.left.right.left = Node("C")
tree.right.left.right.right = Node("Y")
tree.right.right.left.left = Node("Z")
tree.right.right.left.right = Node("Q")
tree.right.right.right.left = Node("")
tree.right.right.right.right = Node("")

getText = input("Enter: ").upper()
morseCode = ""

for char in getText:
    dotanddashes =[]
    encode(tree,char,dotanddashes)
    code = "".join(dotanddashes)
    morseCode = morseCode + code + " "

print(morseCode)