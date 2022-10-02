class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    def traverse(self):
        if(self.start_node==None):
            print("the list is empty")
        else:
            n = self.start_node
            while(n is not None):
                print(n.item)
                n = n.next 
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node 

    def insert_end(self,data):
        new_node = Node(data)
        if(self.start_node is None):
            self.start_node = new_node
        else:        
            n = self.start_node 
            while(n.ref is not None):
                n = n.next
            n.ref = new_node

    def insert_at_index(self,i,data):
        new_node = Node(data)
        n = self.start_node
        cnt = 0       
        while(n is not None):
            if(cnt==i-1):
                break
            else:
                cnt = cnt+1
                n = n.next

        new_node.next = n
        n.ref = new_node 