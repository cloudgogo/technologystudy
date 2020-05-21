# -*- coding: utf-8 -*-
def quadratic(a,b,c):
    if not isinstance(a,(float,int)):
        raise TypeError('a的数据类型错误')
    elif not isinstance(b,(float,int)):
        raise TypeError('b的数据类型错误')
    elif not isinstance(c,(float,int)):
        raise TypeError('c的数据类型错误')
    if pow(b,2)-4*a*c<0:
        return '此方程无解'
    else:
        return set([(-b+(pow(pow(b,2)-4*a*c,1/2)))/2*a,(-b-(pow(pow(b,2)-4*a*c,1/2)))/2*a])

print(f'{quadratic(2,3,1)}')