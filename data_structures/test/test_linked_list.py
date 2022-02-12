import pytest
import linked_list

def test_add():
  list = linked_list.LinkedList()

  list.addFirst("First Element")
  list.addFirst("Second Element")
  list.addFirst("Third Element")

  assert str(list) == "Third Element -> Second Element -> First Element"

def test_remove():
  list = linked_list.LinkedList()

  list.addLast("First Element")
  list.addLast("Second Element")
  list.addLast("Third Element")

  assert list.remove(1) == "Second Element"
  assert str(list) == "First Element -> Third Element"

def test_get():
  list = linked_list.LinkedList()

  list.addLast("First Element")
  list.addLast("Second Element")
  list.addLast("Third Element")

  assert list.get(0) == "First Element"
  assert list.get(2) == "Third Element"