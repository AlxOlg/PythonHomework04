# Вывод в порядке возрастания чисел, которые встречаются в обоих наборах чисел.

# Генерация списка случайных целых чисел.
def gen_list_rnd(n, min_val, max_val):
    import random
    return [random.randint(min_val, max_val) for i in range(n)]

# Вариант 1.
def sort_intersect_list_1(list1, list2):
    return sorted([i for i in set(list1) if i in list2])
# Вариант 2.
def sort_intersect_list_2(list1, list2):
    return sorted(list(set(list1) & set(list2)))
# Вариант 3.
def sort_intersect_list_3(list1, list2):
    return sorted(set(list1).intersection(list2))

min_value = 0
max_value = 100
list1 = gen_list_rnd(int(input('Чисел в первом наборе: ')), min_value, max_value)
list2 = gen_list_rnd(int(input('Чисел во втором наборе: ')), min_value, max_value)
print(list1)
print(list2)
print(sort_intersect_list_1(list1, list2))
print(sort_intersect_list_2(list1, list2))
print(sort_intersect_list_3(list1, list2))