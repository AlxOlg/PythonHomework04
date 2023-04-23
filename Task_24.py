# Максимальное количество ягод с куста + двух соседних, растущих на грядке по кругу.

def gen_array_rnd(n, min_val, max_val):
    import random
    return [random.randint(min_val, max_val) for i in range(n)]

def max_amt(arr):
    max = 0
    for i in range(-1, len(arr) - 1):
        amt = arr[i - 1] + arr[i] + arr[i + 1]
        if amt > max:
            max = amt
    return max

min_value = 0
max_value = 10
N = int(input('Количество кустов в грядке: '))
if N > 2:
    array = gen_array_rnd(N, min_value, max_value)
    print(array)
    print(f'Максимальное количество ягод: {max_amt(array)}')
else:
    print('Кустов должно быть не меньше трех!')
