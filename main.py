# print (5)

# print (5, 8, 6)

# n = 5
# print (n)

# n = None
# print (n)

# n = 1.89
# print (n)

# n = 'helow'
# print (n)

# n = 5
# print(type(n))
# n = "helow"
# print(type(n))

# n = 'he\'low'
# print(n)
# n = '"helow"'
# print(n)

# a = 5
# b = 5.89
# c = 'hello'
# print(a,b,c)

# a = 5
# b = 5.89
# c = 'hello'
# print(a,' - ',b,' - ',c)

# a = 5
# b = 5.89
# c = 'hello'
# print(f"{a} - {b} - {c}")

# a = 5
# b = 5.89
# c = 'hello'
# print("{} - {} - {}".format(a,b,c))

# a = input()
# print(a)

# print("Введите первое значение:")
# a = input()
# b = input('Введите второе значение:')
# print(a ,' + ', b ,' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# n = int(c)
# print(n)
# print(type(n))

# a = int(input("Введите первое значение: "))
# b = int(input("Введите второе значение: "))
# print(a ,' + ', b ,' = ', a + b)

# a = 5.9956
# b = 6.556551
# print(round(a*b, 2))

# username = input("Введите логин: ")
# if username == 'admin':
#         print("ваш пароль 1234")
# elif username == 'user':
#         print("ваш пароль 0000")
# elif username == 'guest':
#         print("ваш пароль 5678")
# else:
#         print("неверный логин")
                                                        
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит!')
# print(i)      

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in 1, 2, 3:
#     print(i)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # -5-4-3-2-1
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# n = 700
# m = 750
# a = int(m%n)
# b = a>0
# c = m//n + b
# print(c)

# a = int(input('Введите кол-во учеников в 1 классе: '))
# b = int(input('Введите кол-во учеников в 2 классе: '))
# c = int(input('Введите кол-во учеников в 3 классе: '))
# if (a+b+c)%2 == 0:
#     print ((a+b+c)//2)
# else:
#     print ((a+b+c)//2+1)

# a = int(input('Введите число: '))
# b = 1
# c = 0
# while c < a:
#    b = b * (c + 1)
#    c += 1
# print(b)

# a = int(input('Введите число: '))
# e = 0
# b = 1
# c = 0
# if a > 0:
#     while e < a:
#         d = b + c
#         b = c
#         c = d
#         e += 1
#     print(c)
# else:
#     print(-1)

# list_1 = []
# list_2 = ()

# list_3 = [1, 2, 3]
# for i in list_3:
#     print(i)
# print(len(list_3))

# list_3 = [1, 2, 3]
# print(list_3[1])

# list_1 = [1, 2, 3]
# print(list_1)
# list_1.append(4)
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(int(input('Введите число: ')))
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))
# print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменятькортеж)

