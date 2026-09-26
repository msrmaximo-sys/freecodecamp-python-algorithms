def hanoi_solver(numero):
    varilla_0 = []
    varilla_1 = []
    varilla_2 = []
    historial_movimiento = []
    varillas = [varilla_0, varilla_1, varilla_2]

    for n in range(numero, 0, -1):
        varilla_0.append(n)

    historial_movimiento.append([varillas[0].copy() ,varillas[1].copy(), varillas[2].copy()])
    movimiento(varillas,0,1,2,numero,historial_movimiento)

    texto = ""
    for m in historial_movimiento:
      texto = texto + str(m[0]) + " " + str(m[1]) + " " + str(m[2]) + "\n"
    
    texto = texto[:-1]
    return (texto)

def movimiento(varillas ,inicio,medio,final, n ,historial_movimiento):
    
    if n == 1:
       sacar = varillas[inicio].pop()
       colocar = varillas[final].append(sacar)
       historial_movimiento.append([varillas[0].copy(), varillas[1].copy(), varillas[2].copy()])

    else:
        movimiento(varillas,inicio,final,medio, n - 1,historial_movimiento)
        sacar = varillas[inicio].pop()
        colocar = varillas[final].append(sacar)
        historial_movimiento.append([varillas[0].copy() ,varillas[1].copy(), varillas[2].copy()])
        movimiento(varillas,medio,inicio,final, n - 1,historial_movimiento)
       
    
    
print(hanoi_solver(4))