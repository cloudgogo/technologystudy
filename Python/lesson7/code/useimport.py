from initfunction import change
from initfunction import my_abs
tup=change('aaaa',11)
a=tup[0]
b=tup[1]
print (a,b)

# >>> from initfunction import my_abs
# a=10000,b=22222
# a=22222,b=10000
# a=10,b=20
# a=20,b=10
# 这里是展示转换结果:a开始为10,b开始为20,结果为[20, 10]
# >>> my_abs(1,2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: my_abs() takes 1 positional argument but 2 were given
# >>> my_abs('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/allen/桌面/workspace/technologystudy/Python/lesson7/code/initfunction.py", line 18, in my_abs
#     if x >= 0:
# TypeError: '>=' not supported between instances of 'str' and 'int'
# >>> abs('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'

