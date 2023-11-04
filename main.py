# # #print(list(inpit().split()).count("2"))
# #
# # # str = "Лена Обь Волга Дон Енисей"
# # # lst = sorted(list(str.split()))
# # # lst.pop(0)
# # # print(lst)
# #
# # # a = [5.4, 6.7, 10.4]
# # # b = "8 11"
# # # lst = list(map(int, b.split()))
# # # a.append(lst)
# # # print(a)
# #
# # # in1 = input()
# # # in2 = input()
# # # in3 = input()
# # # lst1 = list(map(str, in1.split()))
# # # lst2 = list(map(str, in2.split()))
# # # lst3 = list(map(str, in3.split()))
# # # lst = [lst1, lst2, lst3]
# # # print(lst)
# #
# # # in1 = input().split()
# # # in2 = input().split()
# # # in3 = input().split()
# # # print(in1[-1], in2[-1], in3[-1] )
# #
# # #
# # # print(input().split()[-1], input().split()[-1], input().split()[-1] )
# #
# # # a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
# # # print(a[2][1][0])
# #
# # # t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
# # #     ["Я", "Python", "выучил", "с", "каналом"],
# # #     ["Балакирев", "что", "раздавал?"]]
# # # inp = "что"
# # # lst = sum(t,[])
# # # print(lst)
# # # print(inp in lst)
# #
# #
# # # x = list(map(float, input().split()))
# # # if x[0] > x[1]:
# # #     print(x[0])
# # # else:
# # #     print(x[1])
# #
# # # str1 = input().lower()
# # # str2 = str1[::-1]
# # # if str1 in str2:
# # #     print("ДА")
# # # else:
# # #     print("НЕТ")
# #
# # # m, n = map(int, input().split())
# # # if (m % n == 0):
# # #     print(int(m/n))
# # # else:
# # #     print(f"{m} на {n} нацело не делится")
# #
# # # #a, b, c = map(int, input().split())
# # # a, b, c = 3, 4, 5
# # # if a**2 + b**2 == c**2:
# # #     print("ДА")
# # # else:
# # #     print("НЕТ")
# #
# # # a = int(input())
# # # if a % 10 == 7:
# # #     print("ДА")
# # # else:
# # #     print("НЕТ")
# # #
# # # print('НДЕАТ'[input()[-1]=='7'::2])
# #
# # # str = "Python"
# # # str = input().lower()
# # # if str.index("t") >= 0 and str.index("h") >= 0 and str.index("o") >= 0:
# # #     print("ДА")
# # # else:
# # #     print("НЕТ")
# #
# # str = "Python"
# # # str = input().lower()
# # if "t" in str and "h" in str and "o" in str:
# #     print("ДА")
# # else:
# # #     print("НЕТ")
# #
# # lst = list(input().split())
# # if "Москва" in lst:
# #     lst.remove("Москва")
# # print(*lst)
#
# # a, b, c, d = map(int,input().split())
# # if (a > c + 1 and b > d +1) or (a > d +1 and b > c +1):
# #     print("ДА")
# # else:
# #     print("НЕТ")
#
#
# # num = list(map(int, input()))
# # if sum(num[0:3]) == sum(num[3:7]):
# #     print("ДА")
# # else:
# #     print("НЕТ")
# #
# # t = float(input())
# # if  t < 3 or t % 5 < 3:
# #     print("green")
# # else:
# #     print("red")
#
# # m = '''1. Введение в Python
# # 2. Строки и списки
# # 3. Условные операторы
# # 4. Циклы
# # 5. Словари, кортежи и множества
# # 6. Выход'''
# # menu = list(m.split("\n"))
# # c = input()
# # if c == "1":
# #     print(menu[0])
# # elif c == "2":
# #     print(menu[1])
# # elif c == "3":
# #     print(menu[2])
# # elif c == "4":
# #     print(menu[3])
# # elif c == "5":
# #     print(menu[4])
# # elif c == "6":
# #     print(menu[5])
# # else: print("не верный выбор")
#
# # a, b, c = map(int, input().split())
# # if a < b:
# #     if a < c:
# #         print(a)
# #     else: print(c)
# # elif b < c:
# #     print(b)
# # else:
# #     print(c)
#
# # m = float(input())
# # if m <= 60:
# #     print(1)
# # elif m <= 64:
# #     print(2)
# # elif m <= 69:
# #     print(3)
# # else:
# #     print(4)
#
# day = int(input())
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day == 3:
#     print("Среда")
# elif day == 4:
#     print("Четверг")
# elif day == 5:
#     print("Пятница")
# elif day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")

# arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month = int(input())
# if 0 < month <= 12:
#     print(arr[month])
# else:
#     print("Выпей чаю")

# m, n = 8, 1
# # m, n = map(int, input().split())
# day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if n == 1:
#     print(f"{m-1:02}.{day[m-1]:02} {m:02}.{n+1:02}")
# elif n == day[m]:
#     print(f"{m:02}.{n-1:02} {m+1:02}.01")
# else:
#     print(f"{m:02}.{n-1:02} {m:02}.{n+1:02}")

# k = int(input())
# days = ["0", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# print(str(days[k % 7]))

# a = float(input())
# b = float(input())
# print(a if a > b else b)

# a = int(input())
# print(msg := "кратно 3" if int(input()) % 3 == 0 else "не кратно 3")

# text = input().lower()
# print(msg := "палиндром" if text == text[::-1] else "не палиндром")

# print("True" if int(input()) != 0  else "False")

# a = int(input())
# print("0" if a == 59 else a+1)

# m = ['', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# a, b, c = map(int, input().split())
# print(("#"+m[a] if m[a] == ("до" or "фа") else m[a]) + " " +
#       ("#"+m[b] if m[b] == ("до" or "фа") else m[b]) + " " +
#       ("#"+m[c] if m[c] == ("до" or "фа") else m[c]))

# cost = float(input())
# i = 2
# while i <= 10:
#     print(round(cost * i, 1), end=" ")
#     i += 1

# n = int(input())
# i = 1
# s = 0
# while i <= n:
#     s += 1/i
#     i += 1
# print(round(s, 3))

# s = 0
# while (n := int(input())) != 0:
#     s += n
# print(s)

# text = input()
# while "--" in text:
#     text = text.replace("--", "-")
# print(text)

# n = int(input())
# x = 1
# while n > 1:
#     x = x * (n % 10)
#     n = n // 10
# print(x)

# n = int(input())
# lst = [1, 1]
# i = 0
# while i < n-2:
#     lst.append(lst[i] + lst[i+1])
#     i += 1
# print(lst)

'''
Подвиг 9. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить,
сколько клеток будет через n часов (n - целое положительное число, вводимое
с клавиатуры). Считать, что изначально была одна амеба. Результат вывести
на экран. Задачу необходимо решить с использованием цикла while.
Sample Input:
11
Sample Output:
8
'''

# n = int(input())
# a = 1
# while i := 1 <= n:
#     if i % 3 == 0:
#         a *= 2
#     i += 1
# print(a)

'''
Подвиг 10. Гражданин 1 января открыл счет в банке, вложив 1000 руб.
Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
 Определить сумму вклада через n лет (n - целое положительное число, 
 вводимое с клавиатуры). Результат округлить до сотых и вывести на экран. 
 Программу реализовать при помощи цикла while.
Sample Input:
5
Sample Output:
1276.28'''

# n = int(input())
# start = 1000
# i = 1
# while i <= n:
#     start += + start*5/100
#     i += 1
# print(round(start, 2))

'''Подвиг 11. Вводятся два натуральных четных числа n и m в одну строчку через пробел, 
причем n < m. Напечатать все нечетные числа из интервала [n, m]. Задачу
 решить без применения условного оператора. Результат вывести на экран 
 в виде строки чисел, записанных через пробел. Программу реализовать при помощи цикла while.

Sample Input:

2 10
Sample Output:

3 5 7 9'''

# n, m = map(int, input().split())
# while n < m:
#     n += 1
#     print(n, end=" ")
#     n += 1

'''Подвиг 12. Составить программу поиска всех трехзначных чисел, 
которые при делении на 47 дают в остатке 43 и кратны 3. 
Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while.

Sample Input:

Sample Output:

231 372 513 654 795 936'''

# start = 100
# finish = 999
# while start <= finish:
#     if start % 47 == 43 and start % 3 == 0:
#         print(start, end=" ")
#     start += 1

'''Подвиг 2. Имеется одномерный список длиной 10 элементов, состоящий из нулей:p = [0] * 10
На каждой итерации цикла пользователь вводит целое число 
- индекс элемента списка p, по которому записывается значение 1,
 если ее там еще нет. Если же 1 уже проставлена, то список не менять и снова запросить 
 у пользователя очередное число. Необходимо расставить так пять единиц в список. (После этого цикл прерывается).
Программу реализовать с помощью цикла while и с использованием оператора continue, 
когда 1 не может быть добавлена в список. Результат вывести на экран в виде последовательности чисел, записанных через пробел.
Sample Input:
1
2
2
5
7
5
9
Sample Output:
0 1 1 0 0 1 0 1 0 1'''

# p = [0] * 10
# i = 0
# count = 0
# while count < 6:
#     i = int(input())
#     if p[i] == 1:
#         continue
#     else:
#         p[i] = 1
#         count += 1
# print(*p)
