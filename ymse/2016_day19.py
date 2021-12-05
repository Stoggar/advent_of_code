inp = 3014387


### linked list ###
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'Node(value={self.value}, next={self.next_node.value})'

def create_circular_linked_list(n: int):
    node_last = Node(inp)
    node_newest = node_last
    for i in range(inp-1, 0, -1):
        node = Node(i, node_newest)
        node_newest = node
    node_last.next_node = node_newest
    return node_newest

def print_linked_list(n: Node, end_node=None):
    if n == end_node:
        return
    print(n)
    print_linked_list(n.next_node, end_node=n if end_node is None else end_node)

node0 = create_circular_linked_list(inp)
#print_linked_list(node0)
### end linked list ###



#### Elves: ####
node = node0
while True:
    # hvis neste elf er oss selv, har vi endet opp med alle pakkene
    if node == node.next_node:
        print(node)
        break
    # hva er neste elf, rett opp så vi peker på neste etter han
    node.next_node = node.next_node.next_node
    # gå til neste
    node = node.next_node
#### End Elves: ####







