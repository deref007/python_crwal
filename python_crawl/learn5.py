#面向对象的编程
#类：具有某种特征的事物的集合
#对象：群体（类）里面的分体
#类是抽象的，对象是具体的
'''
格式：
class 类名：
     类里面的内容
'''
'''构造函数或者称为构造方法
__init__(self,参数)
在类中的方法必须加上self
其实际意义：初始化
'''
class cla():
    def __init__(self):
        print('I am deref')
a=cla()
'''
给类加上参数：给构造函数加上参数
'''
class cla1():
    def __init__(self,name,job):
        print('my name is ' + name+';'+' my job is '+job)
b=cla1('deref','student')
'''
属性和方法
属性：类里面的变量

'''
class cla2():
    def __init__(self,name,job):
        self.my_name=name
        self.my_job=job
c=cla2('deref','student')
print(c.my_name)
print(c.my_job)
'''
方法：类里面的函数
def 函数名（self，参数）：
'''
class cla3():
    def fun1(self,name):
        print('test a 方法:',name)
d = cla3()
d.fun1('python')
class cla4():
    def __init__(self,name):
        self.my_name=name
    def fun2(self):
        print('hello',self.my_name)
e= cla4('deref')
e.fun2()
'''
继承与重载

'''
#父类：格式：class（基类）
class father():
    def speak(self):
        print('I can speak')
#子类：
class son1(father):
    pass
f=son1()
f.speak()
#母类：
class mother():
    def write(self):
        print('I can write')
#多继承：
class daughter(father,mother):
    def leason(self):
        print('I can leasoning')
g=daughter()
g.speak()
g.write()
g.leason()
#重载：
class son2(father):
    def speak(self):
        print('I can speak fastly')
h=son2()
h.speak()
