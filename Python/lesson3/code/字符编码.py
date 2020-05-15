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

