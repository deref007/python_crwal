#python文件的操作
#打开文件
'''
open(文件地址，操作形式）
w:写入
r:读取
b:二进制
a:追加
'''
#读取：
fh=open('C:\\Users\smallnew\Desktop\commit Guru.txt','r')
#data=fh.read()
line=fh.readline()
print(line)
fh.close()
'''
#写入：
data='deref的翻译commit guru'
fh2=open('C:\\Users\smallnew\Desktop\commit Guru.txt','w')
fh2.write(data)
fh2.close()
'''
'''
异常处理格式：
try：
   程序
except Exception as 异常名称：
    异常处理部分
'''