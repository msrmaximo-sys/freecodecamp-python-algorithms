def verify_card_number(tarjeta):

    tarjeta = tarjeta.replace("-", "")
    tarjeta = tarjeta.replace(" ", "")

    contador = 0
    suma = 0

    for n in range(len(tarjeta) - 1, -1, -1):

        digito = int(tarjeta[n])

        if contador % 2 == 1:
            digito = digito * 2
            if digito > 9:
                digito = digito - 9

        suma = suma + digito
        contador += 1  

    if suma % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
    
    
print(verify_card_number("453914889"))
print(verify_card_number("4111-1111-1111-1111"))
print(verify_card_number("1234 5678 9012 3456"))
print(verify_card_number("453914881"))