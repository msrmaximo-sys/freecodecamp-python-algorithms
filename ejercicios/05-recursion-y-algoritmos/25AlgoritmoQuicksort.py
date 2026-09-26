def quick_sort(array):

    if len(array) <= 1:
     return array

    inicial = array[0]
    menores = []
    iguales = []
    mayores = []

    for n in array:
       if n < inicial:
        menores.append(n)
       elif n > inicial:
        mayores.append(n)
       else:
        iguales.append(n)

    return quick_sort(menores) + iguales + quick_sort(mayores)



quick_sort([83, 4, 24, 2])
quick_sort([4, 42, 16, 23, 15, 8])


print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))