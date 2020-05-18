# Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> classmate=['张三','李四','王五']
# >>> len(classmate)
# 3
# >>> classmate
# ['张三', '李四', '王五']
# >>> classmate[1]
# '李四'
# >>> classmate[0]
# '张三'
# >>> classmate[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> classmate[-1]
# '王五'
# >>> classmate[-2]
# '李四'
# >>> classmate[-3]
# '张三'
# >>> classmate[-4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> classmate.append('luoxiang')
# >>> classmate
# ['张三', '李四', '王五', 'luoxiang']
# >>> classmate.insert(1,'luoxiang')
# >>> classmate
# ['张三', 'luoxiang', '李四', '王五', 'luoxiang']
# >>> classmate.pop()
# 'luoxiang'
# >>> classmate
# ['张三', 'luoxiang', '李四', '王五']
# >>> classmate.pop(2)
# '李四'
# >>> classmate
# ['张三', 'luoxiang', '王五']
# >>> classmate[1]='罗翔'
# >>> classmate
# ['张三', '罗翔', '王五']
# >>> classmate.append(['赵六',16,['teen','武汉']])>>> classmate['张三', '罗翔', '王五', ['赵六', 16, ['teen', '武汉']]]
# >>> len(classmate[3])
# 3
# >>> len(classmate[3][2])
# 2
# >>> unchangeclass=(8,)
# >>> unchangeclass
# (8,)
# >>> unchangeclass[0]
# 8
# >>> unchangeclass[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range
# >>> unchangeclass=('张三', '罗翔', '王五', ['赵六', 16, ['teen', '武汉']])
# >>> unchangeclass[1]'罗翔'
# >>> unchangeclass[0]
# '张三'
# >>> '张三', '罗翔', '王五', ['赵六', 16, ['teen', '武汉']]