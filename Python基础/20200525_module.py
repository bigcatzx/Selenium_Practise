# 调用时间模块
import time
print(time.ctime())

# 直接导入ctime()函数
from time import ctime
print(ctime())

# 直接导入多个函数
from time import ctime, sleep
print(ctime())

# 导入time下所有的函数
from time import *
print(ctime())
sleep(2)
print(ctime())

# 对导入的函数进行重命名
from time import sleep as as_sleep
as_sleep(2)
print(222)