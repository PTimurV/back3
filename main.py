class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class BracketChecker:
    def __init__(self, inputData):
        self.stack = Stack()
        self.opening_brackets = "([{"
        self.closing_brackets = ")]}"
        self.inputData = inputData

    def check(self):
        for index, char in enumerate(self.inputData, start=1):
            if char in self.opening_brackets:
                self.stack.push((char, index))
            elif char in self.closing_brackets:
                if self.stack.is_empty():
                    return index
                top_char, top_index = self.stack.pop()
                if (top_char == "(" and char != ")") or \
                   (top_char == "[" and char != "]") or \
                   (top_char == "{" and char != "}"):
                    return index
        if not self.stack.is_empty():
            top_char, top_index = self.stack.pop()
            return top_index
        return "Success"

# Пример использования
inputData = input().strip()
checker = BracketChecker(inputData)
result = checker.check()
print(result)