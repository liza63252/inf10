def find_intersection(list1, list2):
    intersection = []#Функция находит пересечение двух массивов с помощью двойного цикла
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in intersection:
                intersection.append(num1)
    return intersection            

# Ввод данных
arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

# Вызов функции
result = find_intersection(arr1, arr2)

# Вывод результата
print("Пересечение массивов:", result)
