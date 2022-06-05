class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printError(msg):
    print(f"{bcolors.FAIL} {msg} {bcolors.ENDC}")

def printOK(msg):
    print(f"{bcolors.OKGREEN} {msg} {bcolors.ENDC}")


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class SLL:
    def __init__(self):
        self.head = None 

    def insertByIndex(self, data, index=-1):
        """
        if index is -1, append at end
        0th indexing
        """
        newNode = Node(data)

        if self.head is None:
            if index == 0 or index == -1:
                self.head = newNode 
            else:
                printError("Error: index out of range, no head")
        elif index == 0:
            newNode.next = self.head
            self.head = newNode 
        elif index == -1:
            lastNode = self.head
            while lastNode.next: 
                lastNode = lastNode.next
            lastNode.next = newNode 
        elif index >= 1:
            currentNode = self.head
            for _ in range(index-1): 
                if not currentNode.next:
                    printError("Error: index out of range, has head")
                else:
                    currentNode = currentNode.next 
            newNode.next = currentNode.next 
            currentNode.next = newNode
        else:
            printError("Error: index < -1")

    def readSLL(self):
        node = self.head 
        print("SLL: ", end=" ")
        while node:
            print(node.data, end=" ")
            node = node.next 

    def updateByIndex(self, newData, index):

        if self.head is None:
            if index == 0 or index == -1:
                self.head.data = newData 
            else:
                printError("Error updateByIndex: index out of range, no head")
        elif index == 0:
            self.head.data = newData 
        elif index == -1:
            lastNode = self.head
            while lastNode.next: 
                lastNode = lastNode.next
            lastNode.data = newData 
        elif index >= 1:
            currentNode = self.head
            for _ in range(index): 
                if not currentNode.next:
                    printError("Error updateByIndex: index out of range, has head")
                else:
                    currentNode = currentNode.next 
            currentNode.data = newData
        else:
            printError("Error updateByIndex: index < -1")

    def updateByValue(self, currData, newData):
        currNode = self.head 

        while currNode:
            if currNode.data == currData:
                currNode.data = newData 
                return 
            currNode = currNode.next 

        printError("Error updateByValue: currData value not found")

    def deleteByIndex(self, index):

        if self.head is None:
            print("Error: index out of range, no head")
        elif index == 0:
            self.head = self.head.next
        elif index == -1:
            if self.head.next is None: # only one node in SLL
                self.head = None
                return 
            prevNode = self.head 
            while prevNode.next.next:
                prevNode = prevNode.next 
            prevNode.next = None
        elif index >= 1:
            prevNode = self.head
            for _ in range(index-1): 
                if not prevNode.next:
                    printError("Error: index out of range, has head")
                    return
                else:
                    prevNode = prevNode.next 
            if prevNode.next:
                prevNode.next = prevNode.next.next
        else:
            printError("Error: index < -1")

    def deleteByValue(self, delData):
        if not self.head:
            printError("Error deleteByValue: index out of range, no head")
        elif self.head.data == delData:
            self.head = self.head.next
        else:
            prevNode = self.head 
            while prevNode and prevNode.next:
                if prevNode.next.data == delData:
                    prevNode.next = prevNode.next.next
                prevNode =  prevNode.next
        printError("Error deleteByValue: delData value not found")
    


if __name__ == "__main__":
    sll = SLL() 
    data = [1, 2, 3, 4, 5]

    for datum in data:
        sll.insertByIndex(datum, -1)

    sll.deleteByIndex(66)

    sll.readSLL()


