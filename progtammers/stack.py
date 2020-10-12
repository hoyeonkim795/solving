class Stack(list):
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return False
        return self.stack.pop()

    def peek(self): # top이 가르키는 데이터를 읽는작업
        return self.stack[-1]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False