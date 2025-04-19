class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
        self.size = 0
        self.max_size = 0
        self.min_size = 0
        self.min_items = []
        self.max_items = []
        self.min = None
        self.max = None
    
    def push(self, obj) :
        self.items.append(obj)
        self.top += 1
        self.size += 1
        if self.min is None or obj < self.min:
            self.min = obj
            self.min_items.append(obj)
        if self.max is None or obj > self.max:
            self.max = obj
            self.max_items.append(obj)
        if self.size > self.max_size:   
            self.max_size = self.size
        if self.size < self.min_size:
            self.min_size = self.size
        return True
    def pop(self) :
        if self.top == -1:
            return None
        obj = self.items.pop()
        self.top -= 1
        self.size -= 1
        if obj == self.min:
            if len(self.min_items) > 0:
                self.min = self.min_items.pop()
            else:
                self.min = None
        if obj == self.max:
            if len(self.max_items) > 0:
                self.max = self.max_items.pop()
            else:
                self.max = None
        return obj
    
    def pop_front(self):
        if self.top == -1:
            return None
        obj = self.items[0]
        self.items.pop(0)
        self.top -= 1
        self.size -= 1
        if obj == self.min:
            if len(self.min_items) > 0:
                self.min = self.min_items.pop()
            else:
                self.min = None
        if obj == self.max:
            if len(self.max_items) > 0:
                self.max = self.max_items.pop()
            else:
                self.max = None
        return obj

    def get_min(self):
        if self.min is None:
            return None
        return self.min
    def get_max(self):
        if self.max is None:
            return None
        return self.max
    def get_size(self):
        return self.size
    def get_max_size(self):
        return self.max_size
    def get_min_size(self):
        return self.min_size
    
    def is_empty(self):
        return self.size == 0
    
    def idx(self,obj):
        if obj in self.items:
            return self.items.index(obj)
        else:
            return -1
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if index < 0:
            index = len(self.items) + index
        if index >= len(self.items):
            return None
        return self.items[index]
    
    def __setitem__(self, index, value):
        if index < 0:
            index = len(self.items) + index
        if index >= len(self.items):
            return False
        self.items[index] = value
        return True
    
    def __contains__(self, obj):
        return obj in self.items
    
    def __iter__(self):
        return iter(self.items)
    
    def __next__(self):
        if self.size == 0:
            raise StopIteration
        else:
            return self.items.pop(0)
        
    def __reversed__(self):
        return reversed(self.items)
    
    def __del__(self):
        self.items = []
        self.top = -1
        self.size = 0
        self.max_size = 0
        self.min_size = 0
        self.min_items = []
        self.max_items = []
        self.min = None
        self.max = None
        return True
    def __bool__(self):
        return self.size > 0
    
    def __hash__(self):
        return hash(tuple(self.items))
    
    def __eq__(self, other):
        if isinstance(other, Stack):
            return self.items == other.items
        return False
    
    def __ne__(self, other):
        if isinstance(other, Stack):
            return self.items != other.items
        return True
    
    def __lt__(self, other):
        if isinstance(other, Stack):
            return self.items < other.items
        return False
    
    def __le__(self, other):
        if isinstance(other, Stack):
            return self.items <= other.items
        return False
    
    def __gt__(self, other):
        if isinstance(other, Stack):
            return self.items > other.items
        return False
    
    def __ge__(self, other):

        if isinstance(other, Stack):
            return self.items >= other.items
        return False
    
    def __add__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items + other.items)
        return False
    
    def __sub__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items - other.items)
        return False
    
    def __mul__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items * other.items)
        return False
    
    def __truediv__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items / other.items)
        return False
    
    def __floordiv__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items // other.items)
        return False
    
    def __mod__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items % other.items)
        return False
    
    def __pow__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items ** other.items)
        return False
    
    def __and__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items & other.items)
        return False
    
    def __or__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items | other.items)
        return False
    
    def __xor__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items ^ other.items)
        return False

    def __invert__(self, other):
        if isinstance(other, Stack):
            return Stack(~self.items)
        return False
    
    def __radd__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items + self.items)
        return False
    
    def __rsub__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items - self.items)
        return False

    def __rmul__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items * self.items)
        return False
    
    def __rtruediv__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items / self.items)
        return False
    
    def __rfloordiv__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items // self.items)
        return False
    
    def __rmod__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items % self.items)
        return False
    
    def __rpow__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items ** self.items)
        return False
    
    def __rand__(self, other):

        if isinstance(other, Stack):
            return Stack(other.items & self.items)
        return False
    
    def __ror__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items | self.items)
        return False
    
    def __rxor__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items ^ self.items)
        return False
    
    def __rshift__(self, other):

        if isinstance(other, Stack):
            return Stack(other.items >> self.items)
        return False
    
    def __lshift__(self, other):
        if isinstance(other, Stack):
            return Stack(other.items << self.items)
        return False
