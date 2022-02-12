import array_list

# ArrayList based Stack
class Stack:
  def __init__(self):
    self.stack = array_list.ArrayList()
  
  def push(self, element):
    self.stack.addLast(element)
  
  def pop(self):
    if self.isEmpty():
      raise Exception("Stack is Empty")
  
    return self.stack.removeLast()
  
  def peek(self):
    if self.isEmpty():
      raise Exception("Stack is Empty")

    return self.stack.get(self.size() - 1)
  
  def isEmpty(self):
    return self.stack.size() == 0
  
  def size(self):
    return self.stack.size()