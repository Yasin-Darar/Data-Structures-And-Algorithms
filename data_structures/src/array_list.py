class ArrayList:
  def __init__(self, capacity = 10):
    self.capacity = capacity
    self.array = [None] * self.capacity
    self.length = 0

  def __increaseCapacity(self, scaling_factor = 2):
    new_capacity = self.capacity * scaling_factor
    new_array = [None] * (new_capacity)
    for i in range(self.length):
      new_array[i] = self.array[i]

    self.array = new_array
    self.capacity = new_capacity

  def addLast(self, element):
    if self.length >= self.capacity:
      self.__increaseCapacity()

    self.array[self.length] = element
    self.length+=1
  
  def get(self, idx):
    if idx < 0 or idx >= self.length:
      raise Exception("Invalid Index")

    return self.array[idx]
  
  def remove(self, idx):
    if idx < 0 or idx >= self.length:
      raise Exception("Invalid Index")

    for i in range(idx, self.length):
      self.array[i] = self.array[i + 1]

    self.length -= 1
  
  def removeLast(self):
    if self.size == 0:
      raise Exception("Cannot remove from empty Array")

    temp = self.array[self.length - 1]

    self.array[self.length - 1] = None
    self.length -= 1

    return temp

  def size(self):
    return self.length