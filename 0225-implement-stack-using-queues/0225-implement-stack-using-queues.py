class MyStack:

    def __init__(self):
        self.arr=[]
    def push(self, x: int) -> None:
        self.arr.append(x)
        for i in range(len(self.arr)-1):
            self.arr.append(self.arr.pop(0))
    def pop(self) -> int:
        return self.arr.pop(0) if self.arr else None
    def top(self) -> int:
        return self.arr[0] if self.arr else None
    def empty(self) -> bool:
        return len(self.arr)==0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()