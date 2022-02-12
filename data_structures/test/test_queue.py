import pytest
import queue

def test_enqueue():
  queueTest = queue.Queue()

  queueTest.enqueue("1st Person")
  queueTest.enqueue("2nd Person")
  queueTest.enqueue("3rd Person")

  assert queueTest.size() == 3
  
  assert queueTest.peek() == "1st Person"
  assert str(queueTest) == "1st Person -> 2nd Person -> 3rd Person"

def test_dequeue():
  queueTest = queue.Queue()

  queueTest.enqueue("1st Person")
  queueTest.enqueue("2nd Person")
  queueTest.enqueue("3rd Person")

  assert queueTest.dequeue() == "1st Person"
  assert queueTest.dequeue() == "2nd Person"
  assert queueTest.dequeue() == "3rd Person"

  with pytest.raises(Exception) as ex_queue:
    raise queueTest.dequeue()

  assert ex_queue.value.args[0] == "Queue is Empty"
