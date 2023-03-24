# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

numbers_1 = int(input('Введите сколько будет элементов в списке 1? '))
numbers_2 = int(input('Введите сколько будет элементов в списке 2? '))

list_1 = []
element_count = 1

for _ in range(numbers_1):
  
	list_1.append(int(input(f'Введите элемент {element_count} для первого списка: ')))
  
	element_count = element_count + 1

print(sorted(list_1))

list_2 = []
element_count = 1

for _ in range(numbers_2):
  
	list_2.append(int(input(f'Введите элемент {element_count} для второго списка: ')))
  
	element_count = element_count + 1
print(sorted(list_2))

set_1 = set(list_1)
set_2 = set(list_2)

print(set_1.union(set_2))