#python的三种控制流：顺序结构，条件分支结构，循环结构
'''
if语句：条件分支结构语句
'''
'''
a=10
b=1
if(a>11):
    print(a)
elif(a>5 and a<=18):
    print('a>5 and a<=18')
else:
    print(b)
'''
'''
while语句：循环语句

a=0
while(a<10):
    print('deref')
    a+=1
'''
'''
for语句：循环语句，遍历列表。
    :进行常规循环

a=['se','wq','qe','q']
for i in a:
    print(i)
for i in range(0,10):
    print('hello Beijing')
'''
'''
中断语句：continue:中断一次循环 break:全部直接退出
'''
'''
for i in range(0,10):
    if (i==5):
        continue
    print(i)
'''
'''
for i in range(0,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=' ')
    print()
'''
for i in range(9,0,-1):
    for j in range (i,0,-1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=' ')
    print()
import learn3
learn3.func()