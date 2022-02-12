class Node: 
  def __init__(self, value, prev = None, next = None):
    self.value = value
    self.prev = prev
    self.next = next
  
  def __str__(self):
    return str(self.value)

# Single Linked List with Tail
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.length = 0
  
  def __str__(self):
    return ' -> '.join([str(node) for node in self])
  
  def __iter__(self):
    current = self.head
    while current:
        yield current
        current = current.next
  
  def addFirst(self, element):
    if self.length == 0:
      self.head = self.tail = Node(element, None)
    else:
      self.head = Node(element, None, self.head)

    self.length += 1
   
  def addLast(self, element):
    if self.length == 0:
      self.head = self.tail = Node(element, None)
    else:
      self.tail.next = Node(element, None)
      self.tail = self.tail.next

    self.length += 1
  
  def __traverse(self, idx):
    reverse_iterate = self.length / 2 < idx

    if reverse_iterate: trav = self.tail 
    else: trav = self.head

    current_idx = self.length - 1 if reverse_iterate else 0
    while current_idx != idx:
      trav = trav.next
      
      if reverse_iterate: current_idx -= 1
      else: current_idx += 1
    
    return trav
  
  def get(self, idx):
    if idx < 0 or idx >= self.length:
      raise Exception("Invalid Index")

    current_node = self.__traverse(idx)
    return current_node.value
  
  def remove(self, idx):
    if idx < 0 or idx >= self.length:
      raise Exception("Invalid Index")
    
    if self.length == 1:
      temp = self.head
      self.head = self.tail = None
    elif idx == 0:
      temp = self.head
      self.head = self.head.next

      temp.next = None
    else:
      current_node = self.__traverse(idx - 1)
      temp = current_node.next

      current_node.next = current_node.next.next

      temp.next = None
    
    self.length -= 1
    return temp.value

  def size(self):
    return self.length