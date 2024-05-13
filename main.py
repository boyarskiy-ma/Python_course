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

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

