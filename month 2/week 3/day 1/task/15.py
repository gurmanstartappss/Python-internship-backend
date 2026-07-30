from collections import deque

class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = deque()
        self.forward_stack = deque()
        self.current = homepage

    def visit(self, page):
        self.back_stack.append(self.current)
        self.current = page
        self.forward_stack.clear()

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current

    def current_page(self):
        return self.current 