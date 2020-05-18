#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('中'))
print(chr(25991))
print('\u4e2d\u6587')
# incode
# Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x=b'ABC'
# >>> x.encode('ascii')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'bytes' object has no attribute 'encode'
# >>> 'ABC'.encode('ascii')
# b'ABC'
# >>> 'ABC'.encode('UTF-8')
# b'ABC'
# >>> 'ABC'.encode('GBK')
# b'ABC'
# >>> '中文'.encode('UTF-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> '中文'.encode('GBK')
# b'\xd6\xd0\xce\xc4'
# >>> 

#decode 
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8')
# '中文'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8')
# '中文'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'
# >>> b'\xd6\xd0\xce\xc4'.decode('gbk')'中文'
# >>> b'\xd6\xd0\xce\xc4'.decode('UTF-8')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd6 in position 0: invalid continuation byte

# 相差不应太大
# >>> '中'.encode('utf-8')
# b'\xe4\xb8\xad'
# >>> 
# KeyboardInterrupt
# >>> 
# KeyboardInterrupt
# >>> '中'.encode('utf-8')
# b'\xe4\xb8\xad'
# >>> b'\xe4\xb8\xad\xxx'.decode('utf-8',error=ignore)
#   File "<stdin>", line 1
# SyntaxError: (value error) invalid \x escape at position 12
# >>> b'\xe4\xb8\xad\xxx'.decode('utf-8',errors='ignore')
#   File "<stdin>", line 1
# SyntaxError: (value error) invalid \x escape at position 12
# >>> b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
# '中'
# >>> '中'.encode('utf-8')b'\xe4\xb8\xad'
# >>> b'\xe4\xb8\xad\xxx'.decode('utf-8',errors='ignore')
#   File "<stdin>", line 1
# SyntaxError: (value error) invalid \x escape at position 12
# >>> b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
# '中'

# len判断长度
# >>> len(b'ABC')
# 3
# >>> len('中文')
# 2
# >>> len('中文'.encode('utf-8'))
# 6
# >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6
# >>> len('中文'.encode('gbk'))
# 4

# 文件说名头

# %d
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> '%2d-%2d' % (3.1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: not enough arguments for format string
# >>> '%2d-%2d' % (3.1,23)
# ' 3-23'
# >>> '%2.2f-%2.4f' % (3.1415926,23.1)
# '3.14-23.1000'
# >>> 'Age: %s. Gender: %s' % (25, True)
# 'Age: 25. Gender: True'
# >>> 'gorwth rate :%1.2f %%' % 7
# 'gorwth rate :7.00 %'
# >>> 'gorwth rate :%1.2f%%' % 7
# 'gorwth rate :7.00%'
# >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 'Hello, 小明, 成绩提升了 17.1%'
# >>> 'Hello, {0}, 成绩提升了 {1.1f}%'.format('小明', 17.125)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'float' object has no attribute '1f'
# >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 'Hello, 小明, 成绩提升了 17.1%'
# >>> 


# 1. 在input时需若要作为数字运算,需进行转换,input产出为字符串类型
# 2. 在使用占位符进行格式化时,格式化的数字不能进行运算,需提前进行处理
#   exp:print('小明成绩提升了%1.2f%%' % gorwthrate*100) 这种写法是错误的
lastyearscore= float(input('输入小明去年成绩:\n'))
thisyearscore= float(input('输入小明今年成绩:\n'))
gorwthrate=(thisyearscore-lastyearscore)*100/lastyearscore
print('小明成绩提升了%1.2f%%' % gorwthrate)