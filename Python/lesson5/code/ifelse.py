# age=int(input('plase input you age\n'))
# if age>=18:
#     print('you age is ',age)
#     print('adult')
# else:
#     print('you age is ',age)
#     print('teenager')

# 后续条件应该是非当前条件包含后续条件
# if age>=18:
#     print('you age is ',age)
#     print('adult')
# elif age>=6:
#     print('you age is ',age)
#     print('teenager')
# else:
#     print('you age is ',age)
#     print('kid')

#x=None
#x=0
#x=[]
# x=1
# if x:
#     print ('true')
# else:
#     print ('false')


hight=float(input('请输入身高cm:\n'))
weight=float(input('请输入体重kg:\n'))
bmi=(weight/pow(hight/100,2))
if bmi<18.5:
    print('BMI:',bmi,'\n过轻')
elif bmi<=25:
    print('BMI:',bmi,'\n正常')
elif bmi<=28:
    print('BMI:',bmi,'\n过重')
elif bmi<=32:
    print('BMI:',bmi,'\n肥胖')
else:
    print('BMI:',bmi,'\n严重肥胖')
