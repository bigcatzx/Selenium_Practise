# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(11):
#     if i==5:
#         continue
#     print(i)

# a = 0
# while a < 10:
#     a += 1
#     if a == 5:
#         continue
#     print(a)

for num in range(1,101):
    if num%7==0 or num%10==7 or num//10==7:
        continue
    print(num)

a=17
a//10