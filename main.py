import numpy

# завдвння 1
#
# start = 0
# end = 1000
# step = 1
# A = range(start, end, step)
# print(list(A))

# завдання 2

import numpy as np
# def create_array(*args):
#     variable_array = np.array(args, dtype=int)
#     return variable_array
# int_numbers = create_array(1, 3, 5, 7, 9, 0)
# print(int_numbers)

# завдання 3

# import numpy as np
# def increasing_array(array):
#     return np.sort(array)
# def decreasing_array(array):
#     return np.sort(array)[::-1]
# array = np.array([1, 5, 3, 22, 476, 2])
# sort_incr = increasing_array(array)
# sort_decr = decreasing_array(array)
# print("За зростанням:", sort_incr)
# print("За спаданням:", sort_decr)

# завдання 4

import numpy as np
# def first_array(array1):
#     return np.sort(array1)
# array1 = np.array([3, 6, 2, 55, 0, 31])
#
# def second_array(array2):
#     return np.sort(array2)
# array2 = np.array([8, 5, 4, 99, 12, 333])
#
# array3 = np.concatenate((array1, array2))
# array3 = np.sort(array3)
#
# sort_array1 = first_array(array1)
# sort_array2 = second_array(array2)
#
# print("Перший масив:", sort_array1)
# print("Другий масив:", sort_array2)
# print("Третій масив:", array3)



# def concatenated_array(arr1, arr2):
#     arr1.extend(arr2)
#     arr1.sort()
# arr1 = [4, 1, 56, 15.8]
# arr2 = [66, 2, 3, 57, 32]
# concatenated_array(arr1, arr2)
# print(arr1)

# завдання 5

# import random
# def RandomArray(N):
#     random_array = []
#
#     while len(random_array) < N:
#         random_number = random.randint(1, N)
#         if random_array.count(random_number) == 0:
#             random_array.append(random_number)
#     return random_array
#
# N = 17
# random_numbers_array = RandomArray(N)
# print(random_numbers_array)

# завдання 6

# import numpy as np
# a = np.arange(1.0, 101.0)
# b = a.reshape(10, 10)
# print(b)

#  завдання 7

# import numpy as np
# a = np.arange(1, 101)
# b = a.reshape(10, 10)
# matrix_row =b.reshape(1,100)
# print(matrix_row)

# завдання 8

# import numpy
# def ArrayEight():
#     array_eight = numpy.arange(1, 101)
#
#     def shaping(arr):
#       arr = arr.reshape(1, 100)
#       array_eight_column = arr.reshape(100, 1)
#
#       print(arr)
#       print(array_eight_column)
#
#     shaping(array_eight)
# ArrayEight()

# завдання 9

# import numpy as np
# def multiplying_array(array):
#     multiplying = np.tile(array, 10)
#     print(multiplying)
#
# array = np.array([1, 2, 3])
# multiplying_array(array)

# завдання 10

# import  numpy as np
#
# nul_matrix = np.zeros((10, 10))
#
# print(nul_matrix)

# завдання 11

# import numpy as np
#
# matrix = np.arange(1, 101).reshape(10, 10)
#
# max_elements_columns = np.max(matrix, axis=0)
# min_elements_columns = np.min(matrix, axis=0)
# max_elements_rows = np.max(matrix, axis=1)
# min_elements_rows = np.min(matrix, axis=1)
#
# print(max_elements_columns)
# print(min_elements_columns)
# print(max_elements_rows)
# print(min_elements_rows)

# завдання 12

# import numpy as np
#
# array = np.array([1, -4, 2, 55, -39, 0, -7, -1])
#
# for i, number in enumerate(array):
#     if number < 0:
#         print(f"Номер: {i}, Значення: {number}")

# завдання 13

# array1 = ["телефон", "ноутбук", "мишка", "комп'ютер"]
# array2 = ["пульт", "телефон", "комп'ютер", "навушники"]
# def array3(array1, array2):
#     array3_list = []
#     for word in array1:
#         array3_list.append(word)
#
#     for word in array2:
#         if word not in array1:
#             array3_list.append(word)
#
#     return array3_list
#
# result = array3(array1, array2)
# print(result)

# завдання 14

# months = ["січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень", "вересень",
#           "жовтень", "листопад", "грудень"]
#
# winter = months[0:2] + [months[11]]
# spring = months[2:5]
# summer = months[5:8]
# autumn = months[8:11]
#
# tuple = (winter, spring, summer, autumn)
#
# print(tuple)

# завдання 15

# people = (["Г.А.С.", "28.02.2006"], ["Г.П.С.", "06.06.2008"], ["Р.В.В.", "25.01.2006"])
# def sort_dates(people):
#     dates = people[1]
#     day, month, year = map(int, dates.split('.'))
#     return (year, month, day)
#
# sorted_people = sorted(people, key=sort_dates)
# print(sorted_people)

# завдання 16

# goods = [("phone", 25000, 30), ("laptop", 30000, 25), ("headphones", 7000, 15)]
# order = [("Phone", 30), ("LAPTOP", 3), (" headphones", 15)]
#
# def order_things(order, goods):
#     final_price = 0
#     available_goods = {}
#     for product in goods:
#         product_name = product[0].strip().lower()
#         available_goods[product_name] = (product[1], product[2])
#
#     for product_for_sale in order:
#         product_for_sale_name = product_for_sale[0].strip().lower()
#
#         if product_for_sale_name not in available_goods:
#             return -2
#
#         price, available_nuber = available_goods[product_for_sale_name]
#         number_for_sale = product_for_sale[1]
#
#         if number_for_sale > available_nuber:
#             return -1
#
#         final_price += price * number_for_sale
#
#         available_goods[product_for_sale_name] = (price, available_nuber - number_for_sale)
#
#     return final_price
#
# result = order_things(order, goods)
# if result == -1:
#     print("Запитувана кількість товару перевищує наявну його кількість")
# elif result == -2:
#     print("Tовару із вказаним найменуванням немає в прейскуранті")
# else:
#     print(f"Вартість замовлення: {result}")

# завдання 17

# class Student:
#
# # '''Зберігає особисті дані студента, email, name ...'''
#     def __init__(self, name ="", courses =[], phone_number = "", email_address  = "", degree = ""):
#         self.name = name
#         self.courses = courses
#         self.phone_number = phone_number
#         self.email_address = email_address
#         self.degree = degree
#         print("Створено об’єкт для "+ name)
#
#     def printDetails(self):
# # Виводить атрибути
#         print("Ім’я: ", self.name)
#         print("Курси: ", self.courses)
#         print("Номер телефону:", self.phone_number)
#         print("Email:", self.email_address)
#         print("Рівень освіти:", self.degree)
#
#     def enroll(self, course):
# # Додає навчальні курси
#         self.courses.append(course)
#
# student1 = Student("Mary", ["L548"], "+0632412344", "fygjmhfyf@gmail.com", "Bachelor")
#
# print("Уведіть курси, які вивчає", student1.name)
# newcourse = input("Уведіть номер курсу або 'stop': ")
#
# while newcourse != "stop":
#     student1.enroll(newcourse)
#     print("Уведіть курси, які вивчає", student1.name)
#     newcourse = input("Уведіть номер курсу або 'stop': ")
#
#     student1.printDetails()

# завдання 18

# class Employee:
#
#     def __init__(self, name = "", age = "", position = "", pay = "", prize = ""):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.pay = pay
#         self.prize = prize
#         print("Створено об’єкт для " + name)
#
#     def printDetails(self):
#         print("Ім’я: ", self.name)
#         print("Вік:", self.age)
#         print("Посада:", self.position)
#         print("Заробітна плата:", self.pay)
#         print("Грошова премія:", self.prize)
#
#     def cashPrize(self, prize):
#         self.pay += prize
#         print("Грошова премія + заробітня плата за місяць:", self.pay)
#
# employee1 = Employee("Viktoria", 24, "Teacher", 30000, 25000)
# employee1.printDetails()
# employee1.cashPrize(25000)

















































