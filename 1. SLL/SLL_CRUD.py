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
            node = self.head 
            while node.next:
                node = node.next 
            lastNode = node 
            lastNode.next = newNode 
        elif index > 0:
            prevNode = self.head 
            for _ in range(index - 1):
                if prevNode.next is None:
                    print("Error: index out range, has Head")
                    return
                prevNode = prevNode.next 
            newNode.next = prevNode.next 
            prevNode.next = newNode
        else:
            print("Error: index < -1")

    def readSLL(self):
        currNode = self.head 
        while currNode:
            print(currNode.data, end=" ")
            currNode = currNode.next 

        
if __name__ == "__main__":
    sll = SLL() 

    data = list(range(1, 6))
    for datum in data:
        sll.insertByIndex(datum)

    sll.insertByIndex(200, 5)

    sll.readSLL()
            