"""
 Hello 

"""
from werkzeug.local import LocalStack

# push  pop  top
s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

# 栈 后进先出
s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
