# try...except捕捉异常信息
# try:
#     open("abc.txt",'r')
#     print(a)
# except BaseException as msg:
#     print(msg)

# try:
#     # a = "Exception test!"
#     print(a)
# except NameError as msg:
#     print(msg)
# else:
#     print("No exception here")
# finally:
#     print("Whatever the exception is exist, just run this print!")

# 使用raise抛出异常
# 定义函数
def say_hello(name=None):
    if name is None:
        raise NameError('"name" cannot be empty')
    else:
        print("hello, %s" %name)

say_hello()