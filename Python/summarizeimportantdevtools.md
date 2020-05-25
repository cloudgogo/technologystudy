## python之禅
先说明下为何整理此文档,`python`中对于单一问题的处理经常会有多种解决方式,学习的时候可以兼容并包,但是实际开发中,可能存在使用不同的方案去解决同一问题的情况,这样使得开发变得繁杂,无序  

exp:例如在函数中进行传值,传值为可变长度,可以传输一个`tuple`,`list`,`map`,`set`等容器到函数中,也可以通过在函数定义时使用函数定义的可变参数`*parm`作为参数,在调用时使用`fun(a,b,c)`即可在函数中传递可变参数,在这里函数事实上将获得一个`tuple`类型的`parm`参数,同样在调用时若已存在容器`a=[1,2,3]`,传递时调用可变参数的方法时,可使用`fun(*a)`来代替`fun(a[0],a[1],a[2])`

**事实上,我并不认可可变参数的这套方法,本质上`python`是一种动态语言,灵活性已然很高,我们在传递参数时,传递`list`及`map`即可解决大部分问题,这样的写法虽然简单,但导致程序变化繁杂,既然使用了`Python`,很多问题我认为不需要最优解,而需要通用解,最大程度的降低程序的复杂性,而这篇总结的目的就是为了规范代码提出的通用解**

**python之禅**
```py
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
**translation**
```
Python之禅 by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```
## 数据操作
> 提供数据的格式化操作方式的通用方式
#### 转义
- 转义一般使用`\`即可
- 在`f-string`中,转义`'`或`"`可使用`'''`或`"""`
```py
>>> a='a\nb \\\"\''
>>> print (a)
a
b \"'
```
#### 格式化(在需调用函数时或可使用`f-string`)
符号|含义|特殊方法及备注
:--|:--|:--
%d|格式化为整数|`%2d`无法在数值前补0,一般使用`%d`即可
%f|格式化为小数|`%1.2f`其中`1`也是无用,一般使用`%.2f`即可,需要转义`%`,需使用`%%`
%s|字符串|-
```py
>>> '%2d-%2d' % (3.1,23)
' 3-23'
>>> '%2.2f-%2.4f' % (3.1415926,23.1)
'3.14-23.1000'
>>> 'gorwth rate :%.2f%%' % 7
'gorwth rate :7.00%'
>>> 'gorwth rate :%1.2f%%' % 7
'gorwth rate :7.00%'
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
```
## 函数操作
> 
#### 函数默认参数
定义
```py
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
```
调用
```
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
```
#### 函数传递可变参数
list
```py
>>> def calc(numbers):
...     sum = 0
...     for n in numbers:
...         sum = sum + n * n
...     return sum
... 
>>> calc([1,2,3,4])
30
>>> calc([1,2,3,4,5])
55
```


