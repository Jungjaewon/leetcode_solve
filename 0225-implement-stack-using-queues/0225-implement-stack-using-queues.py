class MyStack:

    def __init__(self):
        from queue import Queue
        self.Q1, self.Q2 = Queue(), Queue()
        self.flip = False
        
    def doflip(self):
        temp_list = list()
        while self.Q1.qsize():
            temp_list.append(self.Q1.get())
        temp_list = temp_list[::-1]
        #print(temp_list)
        for x in temp_list:
            self.Q1.put(x)
        

    def push(self, x: int) -> None:
        
        if self.flip == False:
            self.Q1.put(x)
            print(self.Q1.queue)
        else:
            self.doflip()
            self.Q1.put(x)
            self.flip = False
        
    def pop(self) -> int:
        if self.flip == False:
            self.doflip()
            x = self.Q1.get()
            self.flip = True
            print(f'x : {x}')
            return x
        elif self.flip and self.Q1.qsize():
            x = self.Q1.get()
            self.flip = False if self.Q1.qsize() == 0 else True
            print(f'x : {x}')
            return x
        
    def top(self) -> int:
        if self.flip == False:
            self.doflip()
            self.flip = True
            return list(self.Q1.queue)[0]
        else:
            return list(self.Q1.queue)[0]
        

    def empty(self) -> bool:
        return self.Q1.qsize() == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()