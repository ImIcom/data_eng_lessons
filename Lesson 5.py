
# 1. Написать функцию без параметров.
# 2. Написать функцию с 1 параметром.
# 3. Написать функцию с 3 параметрами.
# 4. Написать функцию с 3 параметрами - и последнему параметру задать значение по умолчанию.
# 5. Функцию с 1 параметром вызвать внутри цикла.
# 6. Написать функцию с 1 параметром - и в этот параметр
#       передать переменную типа list. Функция должна возвращать сумму всех элементов list,
#       который в неё передали. Возвращать через return - а не просто через print выводить.
# 7. Вызвать одну функцию внутри другой.
# 8. Прочитать в интернете, что такое сортировка пузырьком.
#       Написать себе на листке алгоритм, после чего написать функцию,
#       которая на вход получает список (list), сортирует его пузырьком,
#       после чего возвращает отсортированный список.
# Про сортировку пузырьком теория:
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC


list2=[18,8,5,6,3,1,0, 50, 51, 52]
def f1(arr):
    l=len(arr)
    k = 0 # флаг что было перемещение
    for i in range(0, l-1):

        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            k+=1 # если было перемещение, то +1
    print(arr, k)
    return arr, k
def f2(arr2):
    for m in arr2:
        arr2, f = f1(arr2)
        if f==0: #проверяем флаг: если он 0, то нет смысла дальше работать в цикле, выходим раньше.
            return arr2
    return arr2
print(f2(list2))


# def func8(a):
#     for i in a:
#         if a[i]>a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#     return a
#
# print(func8(list2))


# def func7(a):
#     return a*2
# def func77(b,c):
#    result = func7(b) + c
#    return result
# print(func77(2,3))

# def func6(l):
#     sum=0
#     for n in l:
#         sum+=n
#         print(sum)
#     return sum
# list1=[1,2,3,4,5,6,7]
#
# print(f'cумма всех чисел равна {func6(list1)}')

# def func5(a):
#     print(a)
# for n in ['h','e','l','l','o']:
#     func5(n)
#

# def func4(name, sname, tname='TBD'):
#     print(name, sname, tname)
# func4('Владимир', "Петкин")

# def func3(a,b,c):
#     import math
#     d=(b * b) - (4 * a * c)
#     print(d)
#     if d>0:
#         x1 = (-b + math.sqrt(d)) / 2 * a
#         x2 = (-b - math.sqrt(d)) / 2 * a
#         print(x1,x2)
#     elif d == 0:
#         x = - (b / 2 * a)
#         print(x)
#     else:
#         print('Korney net')
# func3(2,4,2)

# def func2(name):
#     print(f'Hello {name}!')
# func2(name='Jack')

# def func1():
#     print('Hello world!')
# func1()