import stack

def test_push():
  stackTest = stack.Stack()

  stackTest.push("Bottom")
  stackTest.push("Middle")
  stackTest.push("Top")

  assert stackTest.size() == 3
  assert stackTest.peek() == "Top"

def test_pop():
  stackTest = stack.Stack()

  stackTest.push("Bottom")
  stackTest.push("Middle")
  stackTest.push("Top")

  assert stackTest.pop() == "Top"
  assert stackTest.pop() == "Middle"
  assert stackTest.size() == 1