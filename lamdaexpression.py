# lambda expression
# jun chai expression chai execute huncha ani result chai return huncha 
#  jastai example,
x = lambda a : a + 10
print(x(5))

x = lambda a,b,c:a+b+c
print(x(2,3,4))

def mul(n):
    return lambda a :a * n

sam = mul(2)
print(sam(2))