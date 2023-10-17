def print_array(array):
    for i in range(N):
        print(f"{array[i]} ")

def get_col_sum(array, column_num):
    res = 0
    for i in range(len(array)):
        res = res + array[i][column_num]
    return res

def swap_col(array, column1, column2):
    for i in range(len(array)):
        array[i][column1], array[i][column2] = array[i][column2], array[i][column1]

def sort_array(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if get_col_sum(array, j) < get_col_sum(array, j + 1):
                swap_col(array, j, j + 1)
    print_array(array)

N = int (input("Введіть розмірність масива-"))
mas = []
for i in range(N):
    row = (input(f"Введіть {N} цілих чисел у рядок через пробіл-" )).split()
    for i in range(len(row)):
        row[i] = int(row[i])
    mas.append(row)
print ("Невідсортований масив")
print_array(mas)
print ("Відсортованний масив")
sort_array(mas)