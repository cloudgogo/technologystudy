# 布尔值 Boolean
True
False
3>2
3>5
3==3

# Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> True
# True
# >>> False
# False
# >>> 3>4
# False
# >>> 3===4
#   File "<stdin>", line 1
#     3===4
#        ^
# SyntaxError: invalid syntax
# >>> 3==4
# False
# >>> 3=4
#   File "<stdin>", line 1
# SyntaxError: cannot assign to literal
# >>> 

# 布尔值参与与或非运算
print(
'tat',True and True,
'\ntaf',True and False,
'\nfaf',False and False,
'\ncaltest',3>1 and 4>3,
'\ntof',True or False,
'\ntor',True or True,
'\nfof',False or False,
'\nnt',not True,
'\nnf',not False,
)
age=12
if age>=18:
    print('adult');
else:
    print('teen');
# 空值
user=None

# 变量
a=1
t_007='T00=7'
Anser=True

# 变量赋值类型可不同(Python为动态语言)
a=123
print (a)
a='abc'
print (a)
# '='为赋值 '=='为判断
x=10
x=x+2
print(x)

# 赋值为将指向修改,并未新增 a,b都是变量,'abc'与'xyz'都创建了,a指向'abc',b指向'abc',a修改指向后,b并未修改
# 实际执行时,a->'abc',b->'abc',a->'xyz',并非a->'abc',b->a
a='abc'
b=a
a='xyz'
print(b)

# 常量: python不存在final概念,实际python并无常量,通常用大写字母表达概念,说明字段是一个不应该变动的结果,是一个规范,同linux文件命名规范
PI=3.1415926

# 除法与精确度问题,整数相除必定是精确的(某些大数在静态语言中并不能表示出来,这里并不清楚Python的情况,不做评论),原因是整数必定是可以用2进制精确表示的,而浮点数无法精确表示,故在进行相除前,整数的信息未丢失,而浮点数的信息丢失导致
# 除/与地板除//,取模运算%
# 这里需要说明一下,取模运算与取余运算不同,%在不同语言中意义不同,比如c/c++，java 为取余，而python则为取模。
# 求模运算和求余运算在第一步不同: 取余运算在取c的值时，向0 方向舍入(fix()函数)；而取模运算在计算c的值时，向负无穷方向舍入(floor()函数)。
# 例如计算：-7 Mod 4
# 那么：a = -7；b = 4；
# 第一步：求整数商c，如进行求模运算c = -2（向负无穷方向舍入），求余c = -1（向0方向舍入）；
# 第二步：计算模和余数的公式相同，但因c的值不同，求模时r = 1，求余时r = -3
print(-7%4)
a=-10
b=3
print(a/b)
print(a//b)
print(a==(a//b)*b+a%b)
# python内部规避了相关问题
print(a==(a/b)*b)
# 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）