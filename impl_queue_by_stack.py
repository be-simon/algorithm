# stack 2개로 queue 구현하기
# dequeue 실행시 스택_1에 쌓인 아이템들을 거꾸로 스택_2에 넣은 후 하나를 꺼낸다.
# 스택_2에 아이템이 있다면 거기서 꺼내면 된다.

class stack:
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, v):
        self.stack.append(v)
        self.len += 1

    def pop(self):
        self.len -= 1
        return self.stack.pop()

class queue_madeby_stack:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
        self.len = 0

    def enqueue(self, v):
        self.stack1.push(v)
        self.len += 1

    def dequeue(self):
        if self.len == 0:
            return -1
        
        self.len -= 1
        if self.stack2.len == 0: # stack1에서 거꾸로 2에 넣는다.
            while self.stack1.len > 1:
                self.stack2.push(self.stack1.pop()) 
            return self.stack1.pop()
        else:
            return self.stack2.pop()

queue = queue_madeby_stack()
items = [1,4,2,7,3,5,9]
for i in items:
    queue.enqueue(i)
while queue.len > 0:
    print(queue.dequeue())