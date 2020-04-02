# Fixing bug in multiply function

def multiply(a, b):
  # a * b Functions without an explicit 'return' statements returns None.
  return a * b

answer = multiply(2, 10)
print(answer)