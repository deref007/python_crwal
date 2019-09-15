#正则表达式：
#原子是正则表达式中最基本的组成单位，每个正则表达式至少要包含一个原子。
import re
#string='deref'
#普通字符作为原子

#非打印字符作原子
#\n：换行符  \t：制表符

#通用字符作为原子
#\w:字母、数字、下划线
#\W:除字母、数字、下划线
#\d： 十进制数字
#\D 除十进制
#\s:空白字符
#\S:除空白字符
'''
string='deref521wyy'
pat="\d\d\d"
rst=re.search(pat,string)
print(rst)
#原子表
'''
'''
元字符
.除换行符外任意字符
^ 匹配开始位置
$ 匹配结束位置
* 匹配0\1\多次
？匹配0\1次
+ 匹配1\多次
｛n｝ 恰好n次
｛n,}至少n次
｛n,m} 至少n 至多m
| 模式选择符
（）模式单元
'''
'''
string='deref5211wyyderef'
pat="de..."
pat="^deref"
pat='wyy$'
pat='deref...*'
pat='deref?'
pat='y+'
pat='deref521?'
rst=re.search(pat,string)
print(rst)
'''
'''
模式修正符
I 匹配时忽略大小写
M 多行匹配
S 让.匹配包括换行符
L 本地化识别匹配
U unicode

'''
string = 'Python'
pat = 'pyt'
rst=re.search(pat,string,re.I)
print(rst)
'''
贪婪模式与懒惰模式
'''
'''
string='djdjuyiaaade'
pat1='dj.*'
pat2='dj.*?'
rst1=re.search(pat1,string,re.I)#贪婪
rst2=re.search(pat2,string,re.I)
print(rst2)
print(rst1)
'''
'''
正则表达式函数
'''
#re.match()#从头开始匹配
string='deref521wyy'
pat1='d.*'
rst1=re.match(pat1,string,re.I)
print(rst1)
'''
全局匹配函数：
re.compile(正则表达式）.findall(数据)
'''
string='safasafwhafaushhash'
pat2='a.*?f'
rst2=re.compile(pat2).findall(string)
print(rst2)
'''
匹配网址 电话号码

'''
string="<a href='http://www.baidu.com'>百度首页</a>'"
pat3='[a-zA-Z]+://[^\s]*[.com|.cn]'
rst3=re.compile(pat3).findall(string)
print(rst3)
string='dtequeeqo153-21387872ydysa4561-541513513213udderf'
pat4='\d{4}-\d{7}|\d{3}-\d{8}'
rst4=re.compile(pat4).findall(string)
print(rst4)
