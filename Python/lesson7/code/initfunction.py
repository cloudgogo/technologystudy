# -*- coding: utf-8 -*-
def change(a,b):
    print('a=%s,b=%s' % (a,b))
    a,b=b,a
    print('a=%s,b=%s' % (a,b))
    return [a,b]
change(10000,22222)

# pass作为占位符,程序可正常运行
def no():
    pass

a=10
b=20
print(f'这里是展示转换结果:a开始为{a},b开始为{b},结果为{change(a,b)}')

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x