import re


class Interpreter:

    def __init__(self, stack):
        self.stack = stack

    def interpret(self, text):
        self.getoperator(text)
        self.getmanipulation(text)
        self.getdigits(text)
        self.selectfunction()
        self.clearvariables()

    def clearvariables(self):
        self.operator, self.manipulation, self.digits = None, None, None

    def getdigits(self, text):
        try:
            self.digits = int(re.search(r'\d+', text).group(0))
        except AttributeError:
            self.digits = None

    def getoperator(self, text):
        self.operator = re.sub(r"\w", "", text, flags=re.I)

    def getmanipulation(self, text):
        self.manipulation = " ".join(re.findall("[a-zA-Z]+", text))

    def selectfunction(self):
        if self.operator and not self.digits:
            self.operation()
        elif self.manipulation:
            self.commandoperation()
        else:
            print("Please input valid command")

    def commandoperation(self):
        func = self.manipulation.lower()
        getattr(self, func)()

    def push(self):
        self.stack.append(self.digits)

    def pop(self):
        self.stack = self.stack[:-1]

    def swap(self):
        end2 = self.stack[-2]
        end1 = self.stack[-1]
        self.stack.pop(-1)
        self.stack.pop(-1)
        self.stack.append(end1)
        self.stack.append(end2)

    def dup(self):
        end1 = self.stack[-1]
        self.stack.append(end1)

    def operation(self):
        operators = {
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y),
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y)}
        self.stack.append(round((operators[self.operator](self.stack[-2], self.stack[-1])), 2))

    def processinput(self):
        self.text = input('fifth> ')
        self.interpret(self.text)
        self.result = self.stack
        print(self.result)

def main():
    stack = [4, 5, 8, 6]
    interpreter = Interpreter(stack)
    while True:
        try:
            interpreter.processinput()
        except:
            break

if __name__ == '__main__':
    main()
