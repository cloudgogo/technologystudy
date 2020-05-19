names=['charles','bob','star']
for name in names:
    print(name)

# 说明:通过缩进确定执行范围,下例子若print(sum)加一缩进则会循环输出
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)

print(list(range(100)))

sum=0
for x in range(101):
    sum=sum+x
print(sum)

sum=0
n=100
while n>0:
    sum=sum+n
    n=n-1
print (sum)

# practice
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,',name,'!\n')

n=1
while n<100:
    print (n)
    if n==10:
        break
    n=n+1

n=1
while n<100:
    n=n+1
    if n % 2!=0:
        continue
    print (n)
    
# n=1
# while n>=1:
#     n=n+1
#     print(n)