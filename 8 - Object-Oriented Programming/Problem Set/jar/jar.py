import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size
    
    def deposit(self, n):
        self.size += n
            
    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        # print("Test Capacity Getter")
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        # print("Test Capacity Setter")
        if type(capacity) != int:
            raise TypeError("A jar's capacity must be an integer")
        elif capacity < 0:
            raise ValueError("A jar cannot have a negative capacity for cookies")
        self._capacity = capacity
    
    @property
    def size(self):
        # print("Test Size Getter")
        return self._size
    
    @size.setter
    def size(self, size):
        # print("Test Size Setter")    
        self._size = size
        if self.size > self.capacity:
            raise ValueError("The number of cookies exceeds the jar's capacity for cookies")
        if self.size < 0:
            raise ValueError("You cannot withdraw any more cookies")
