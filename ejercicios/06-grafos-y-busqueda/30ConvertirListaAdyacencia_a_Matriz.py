def adjacency_list_to_matrix(nodo):
    cantidad = len(nodo)
    matriz = [[0] * cantidad for x in range(cantidad)]
    for origen in nodo:
        for n in nodo[origen]:
            matriz[origen][n] = 1

    for fila in matriz:
        print(fila)
    return matriz


grafo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

resultado = adjacency_list_to_matrix(grafo)
print(resultado)