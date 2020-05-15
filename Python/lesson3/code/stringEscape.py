string='这里是\"以及\'及\\的显示,换行输出制表符空格及使用\"r\'\'\"进行转义\n\t'
print(string,r'\人\'r"w\n""\'w')
# 经测试,在r''中单独使用使用'会出现问题,不推荐使用

# 在命令行中测试结果,其中在解释器中当进行折行时自动补全了print的括号)存在问题
# allen@allen-ThinkPad-T430:~/桌面/workspace/techno
# logystudy$ python
# Python 3.8.2 (default, Mar 13 2020, 10:14:16) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print('''line1)
# ... line2
# ... line3''')
# line1)
# line2
# line3
# >>> print(r'''line1,\n)
# ... line2
# ... test''')
# line1,\n)
# line2
# test
# >>> print('''line1,\n
# ... line2
# ... line3''')
# line1,

# line2
# line3
# >>> 

