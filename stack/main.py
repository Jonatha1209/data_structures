class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []
        self.max_stack = []
        self.size = 0             
        self.max_size = 0        

    def push(self, value):
        self.items.append(value)
        self.size += 1
        
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        
        if self.size > self.max_size:
            self.max_size = self.size

    def pop(self):
        if self.is_empty():
            return None
        
        value = self.items.pop()
        self.size -= 1
        
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        
        return value

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

    def get_max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None

    def get_size(self):
        return self.size

    def get_max_size(self):
        return self.max_size

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return self.size
