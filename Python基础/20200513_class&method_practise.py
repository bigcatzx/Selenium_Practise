# 定义MyClass类
# class MyClass(object):
#     def say_hello(self, name):
#         return "hello, " + name

# 调用MyClass类
# mc = MyClass()
# print(mc.say_hello("Glen"))

# 初始化类
class A:
    def __init__ (self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        # print(self.a + self.b)
        return self.a + self.b
# 调用类时需要传入初始化参数
# count = A('4', 5)
# print(count.add())

# B类继承A类
class B(A):
    # def sub(self, a, b):
    #     return a - b
    def add(self):
        super(B, self).add()
        print(self.a + self.b + 10)
print(B(2,3).add())
# print(B(2,3).sub(2,3))