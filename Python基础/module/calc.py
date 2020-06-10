import sys
from os.path import abspath
print("This file's abs'path is:")
print(abspath(__file__))

def add(a, b):
    return a+b

if __name__ == '__main__':
    # 测试代码 if __name__ == '__main__'代表该模块被其他程序文件调用时，下面的代码不执行
    c = add(2,1)
    print(c)