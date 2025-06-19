class MyQueue:
    def __init__(self):
        self.arr=[]
        self.arr1=[]
    def push(self, x: int) -> None:
        self.arr.append(x)
    def pop(self) -> int:
        if not self.arr1:
            while self.arr:
                self.arr1.append(self.arr.pop())
        return self.arr1.pop() if self.arr1 else None
    def peek(self) -> int:
        if not self.arr1:
            while self.arr:
                self.arr1.append(self.arr.pop())
        return self.arr1[-1] if self.arr1 else None
    def empty(self) -> bool:
        return len(self.arr1)==0 and len(self.arr)==0
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()