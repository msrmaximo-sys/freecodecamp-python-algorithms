def dfs(adyacencia, nodo):
    pila = [nodo]
    visitados = []

    while pila:
        actual = pila.pop()
        
        if actual not in visitados:
            visitados.append(actual)

            for indice,valor in enumerate(adyacencia[actual]):
                if valor == 1:
                    pila.append(indice)
                    
    return visitados
                
                
                
print(dfs([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
], 1))