class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class linkedlist:
    def __init__(self, *args):
        self.length = 0
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.head = Node(args[i])
                    temphead = self.head
                else:
                    temphead.next = Node(args[i])
                    temphead = temphead.next
                self.length += 1
        else:
            self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temphead = self.head
            while temphead.next: temphead = temphead.next
            temphead.next = Node(data)
        self.length += 1
    
    def insert(self, idx, data):
        if abs(idx) >= self.length:
            if idx >= 0: idx = self.length
            else: idx = -self.length
        if idx == 0 or -idx == self.length:
            temphead = self.head
            self.head = Node(data)
            self.head.next = temphead
        else:
            prevhead = self.get(idx-1)
            targethead = prevhead.next
            prevhead.next = Node(data)
            prevhead.next.next = targethead
        self.length += 1

    def pop(self, idx=None):
        if not self.head:
            raise IndexError('pop from empty list')
        else:
            if idx != None:
                if abs(idx) > self.length or idx == self.length:
                    raise IndexError('pop index out of range')
                elif idx == 0 or -idx == self.length:
                    popnode = self.head
                    self.head = self.head.next
                else:
                    prevhead = self.get(idx-1)
                    popnode = prevhead.next
                    targethead_next = popnode.next
                    prevhead.next = targethead_next
            else:
                if self.head.next == None:
                    popnode = self.node
                    self.head = None
                else:
                    prevhead = self.get(self.length-2)
                    popnode = prevhead.next
                    prevhead.next = None
        self.length -= 1
        return popnode
    
    def get(self, idx):
        if abs(idx) > self.length or idx == self.length:
            raise IndexError('list index out of range')
        elif idx < 0:
            idx -= -self.length
        temphead = self.head
        for i in range(idx):
            temphead = temphead.next
        return temphead

    def __repr__(self):
        string = []
        temphead = self.head
        while temphead:
            string.append(temphead.data)
            temphead = temphead.next
        return str(string)
