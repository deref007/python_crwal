print("hello python")
a=9
print(a)
#python的数据类型
#数字 字符串 列表（list)[] 元组（tuple）() 集合（set） 字典（dictionary）
deref="努力学习，积极向上"
print("deref:",deref)
deref=['phone',153,2138,7872]
print(deref)
print(deref[0])
deref[0]='phone-number'
print(deref)
#列表可以重新赋值，元组不行
#字典{key:value,...}
message={'name':"deref","age":'23','address':'beijing'}
print(message['name'])
print(message['address'])
#集合:去重
e=set('abdgsghayenchak')
f=set('adasfiehbajhuyai')

g='e'and 'f'
print(g)
print(e)
#运算符+-*/%
h=5+9*3-10
print(h)
if(h>=10):
    print(h)
