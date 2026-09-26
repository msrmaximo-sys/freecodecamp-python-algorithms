def selection_sort(array):
    for i in range(len(array)):
        menor = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor]:
                menor = j

        if menor != i:
            array[i], array[menor] = array[menor], array[i]

    return array



print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))


lista = [5, 2, 8, 1]

resultado = selection_sort(lista)

print(lista)
print(resultado)
print(lista is resultado)

print(selection_sort([]))
print(selection_sort([7]))