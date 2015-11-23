'''

该脚本的使用必须将代码置于你所要进行操作的文件夹。
这里，对于代码做一点简单的说明：
代码段一：
这里我们通过使用os模块里面的getcwd()方法获取当前脚本所在文件夹路径，然后我们通过listdir()将该文件夹下所有文件的文件名列出来放在一个列表中去。之后的for循环，我们是通过os.path.join()将文件名与文件路径组合在一起，以方便之后的文件的打开。
代码段二：
我们通过Python的文件操作，以追加方式打开这个文件，之后我们去遍历整个文件夹，因为这里我们只是要cpp以及.h头文件里面的代码，所以通过获取文件的后缀名，判断是否符合，符合我们的条件之后我们将用只读方式打开文件，然后读取文件内容，将文件内容追加到我们之前建的文件即可。
'''
#coding:utf-8
import os
##获取当前文件夹
#
filePath = os.getcwd()
#获取当前文件列表
fileNameList = os.listdir(filePath)
fileDirList = []
#获取文件路径列表
for fileName in fileNameList:
    fileDirList.append(os.path.join(filePath, fileName))
#--------����ζ�
f = open('code.txt', 'w')
f.write("开始读文件\n")
f.close()
for code in fileDirList:
    f = open('code.txt', 'a')
    split = os.path.splitext(code)
    if(split[1] == '.h' or split[1] == '.cpp'):
        fz = open(code, 'r')
        string = "源代码文件" + code +"代码::\n"
        f.write(string)
        content = fz.read()
        print "文件 %s 读写成功" % code
        f.write(content)
        fz.close()
    f.close()
 
print "读写完成"