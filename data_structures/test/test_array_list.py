import pytest
import array_list

def test_add():
  array = array_list.ArrayList()

  array.addLast(1)
  array.addLast(3)
  array.addLast(2)
  array.addLast(4)

  assert array.size() == 4

def test_remove():
  array = array_list.ArrayList()

  array.addLast(1)
  array.addLast(3)
  array.addLast(2)
  array.addLast(4)
  array.addLast(1)
  array.addLast(3)
  array.addLast(2)
  array.addLast(4)
  
  array.remove(0)
  assert array.size() == 7

  with pytest.raises(Exception) as ex_array:
    raise array.remove(-1)

  assert ex_array.value.args[0] == "Invalid Index"

  array.remove(1)
  assert array.get(1) == 4

def test_get():
  array = array_list.ArrayList()

  with pytest.raises(Exception) as ex_array:
    raise array.get(1)

  assert ex_array.value.args[0] == "Invalid Index"

  array.addLast(1)
  array.addLast(5)

  assert array.get(1) == 5