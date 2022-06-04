class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class SLL:
    def __init__(self):
        self.head = None 

    def insertByIndex(self, data, index=-1):
        newNode = Node(data) 

        if self.head is None:
            if index == 0 or index == -1:
                self.head = newNode 
            else:
                print("Error: index out of range, no Head") 
        elif index == 0:
            newNode.next = self.head 
            self.head = newNode 
        elif index == -1:
            lastNode = self.head 
            while lastNode.next:
                lastNode = lastNode.next 
            lastNode.next = newNode 
        elif index > 0:
            #10 20 30 40 50->None
            prevNode = self.head
            for _ in range(index - 1):
                if not prevNode.next:
                    print("Error: index out of range, has Head")
                    return 
                prevNode = prevNode.next
            newNode.next = prevNode.next 
            prevNode.next = newNode
        else:
            print("Error: Invalid index, index < -1")

    def readSLL(self):
        node = self.head 
        while node:
            print(node.data, end=" ")
            node = node.next
        
    
if __name__ == "__main__":
    sll = SLL() 

    data = list(range(1, 6))

    for datum in data:
        sll.insertByIndex(datum, -1) 

    sll.insertByIndex(100, -5)

    sll.readSLL()