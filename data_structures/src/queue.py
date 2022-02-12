import linked_list

# LinkedList based Queue
class Queue:
  def __init__(self):
    self.queue = linked_list.LinkedList()
  
  def __str__(self):
    return str(self.queue)
  
  def enqueue(self, element):
    self.queue.addLast(element)
  
  def dequeue(self):
    if self.isEmpty():
      raise Exception("Queue is Empty")

    return self.queue.remove(0)
  
  def peek(self):
    if self.isEmpty():
      raise Exception("Queue is Empty")

    return self.queue.get(0)
  
  def isEmpty(self):
    return self.queue.size() == 0
  
  def size(self):
    return self.queue.size()
