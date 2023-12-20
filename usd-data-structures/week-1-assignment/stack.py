#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max = float('-inf')
        self.aux = []

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.max:
            self.aux.append(a)
            self.max = a

    def Pop(self):
        assert(len(self.__stack))
        top = self.__stack.pop()
        if top == self.max:
            self.aux.pop()

            if self.aux:
                self.max = self.aux[-1]
            else:
                self.max = float('-inf')

    def Max(self):
        assert(len(self.__stack))
        return self.max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
