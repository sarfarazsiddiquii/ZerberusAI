'''
Question: Implement a queue using two stacks.

Assumptions made:

that i can call elements from array/list like this:

a = [1, 2, 3, 4, 5]

lastelement = a[-1] ---- assuming i can use such behaviour in the code.
'''


class Stack:
    """
    mimicking the stack behaviour with array operations.
    """
    def __init__(self):
        self.data = []
        self.top = 0
        
    def pushelement(self, x): 
        new_data = [None] * (self.top + 1) 
        
        for i in range(self.top):
            new_data[i] = self.data[i]
            
        new_data[self.top] = x
        
        self.data = new_data
        self.top += 1
        
        
    def is_stack_empty(self):
        return self.top == 0
    
    
    def popelement(self):
        if self.is_stack_empty():
            return ("Can't Pop from empty stack, try adding numbers")
        
        popped_element = self.data[self.top - 1]
        
        new_size = self.top - 1
        
        new_data = [None] * new_size
        
        for i in range(new_size):
            new_data[i] = self.data[i]
            
        self.data = new_data
        self.top -= 1
        
        return popped_element

    
    def peekfunction(self):
        if self.is_stack_empty():
            return ("Can't Peek from empty stack, try adding numbers")
        return self.data[self.top - 1]
    
    
class MyQueue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
        
    def enqueue(self, x):
        self.stack_one.pushelement(x)
        
    def _transfer_stack_one_to_stack_two(self):
        while not self.stack_one.is_stack_empty():
            element = self.stack_one.popelement()
            self.stack_two.pushelement(element)
        
    def dequeue(self):
        if self.stack_two.is_stack_empty():
            self._transfer_stack_one_to_stack_two()
        return self.stack_two.popelement()
    
    def peek(self):
        if self.stack_two.is_stack_empty():
            self._transfer_stack_one_to_stack_two()
        return self.stack_two.peekfunction()
    
    def is_empty(self):
        if self.stack_one.is_stack_empty() and self.stack_two.is_stack_empty():
            return True
        else:
            return False
            
