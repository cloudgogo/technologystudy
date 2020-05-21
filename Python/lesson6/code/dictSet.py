d={'charles':22,'lele':21,'wang':33}
print(d['charles'])
f={1:14,2:13,3:19}
print(f[1])
f={1:14,2:13,3:19,2:'2333','test':2}
print(f[2])
a=float(input('请输入key'))
# if a in f:
#     print(f[a])

# if f.get(a)!=None:
if f.get(a,-1)!=-1:
    print(f[a])
print(f)
f.pop(2)
print(f)

# >>> d={[1,2,3]:2,1:3}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# >>> d={}
# >>> key=[1,2,3]
# >>> d[key]=2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# >>> key=1
# >>> d[key]='1111'
# >>> d
# {1: '1111'}
# >>> key=2
# >>> d[key]='test'
# >>> d
# {1: '1111', 2: 'test'}
# >>> d.pop(2)
# 'test'
# >>> d
# {1: '1111'}

# >>> s={1,2,3,4}
# >>> s
# {1, 2, 3, 4}
# >>> a=set([1,2,3,4])
# >>> a
# {1, 2, 3, 4}
# >>> a.add(4)
# >>> a
# {1, 2, 3, 4}
# >>> a.add(5)
# >>> a
# {1, 2, 3, 4, 5}
# >>> a.pop(3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: pop() takes no arguments (1 given)
# >>> a.remove(3)
# >>> a
# {1, 2, 4, 5}

s1={1,2,3,4}
s2={2,4,5,7}
print(s1&s2)
print(s1|s2)

# >>> s={[1,2,3],1,2}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

# >>> a={(1,2,3):1}
# >>> a[(1,2,3)]
# 1
# >>> a={(1,[2,3]):1}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'