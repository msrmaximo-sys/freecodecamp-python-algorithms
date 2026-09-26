def validate_isbn(isbn, length):
    # Verifica que la longitud del ISBN coincida con la indicada por el usuario.
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Separa los dígitos principales del dígito de control (check digit).
    # Ejemplo ISBN-10:
    # 1530051126
    # ---------^ -> check digit
    # ^^^^^^^^^ -> main digits
    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    # Convierte los dígitos principales a enteros.
    # Si encuentra un carácter no numérico (por ejemplo '-'),
    # muestra un mensaje y termina la función.
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    # Calcula el dígito de control esperado.
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compara el dígito calculado con el ingresado.
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # Calcula el dígito de control para ISBN-10.
    digits_sum = 0

    # Multiplica cada dígito por un peso descendente de 10 a 2.
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    # Ajusta el resultado según las reglas del ISBN-10.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Calcula el dígito de control para ISBN-13.
    digits_sum = 0

    # Multiplica alternadamente por 1 y por 3.
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    # Si el resultado es 10, el dígito de control es 0.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')

    # Divide la entrada usando la coma.
    # Ejemplo:
    # "1530051126,10" -> ["1530051126", "10"]
    values = user_input.split(',')

    # Intenta obtener el ISBN y la longitud.
    try:
        isbn = values[0]
        length = int(values[1])

    # Si falta la coma o la longitud, se produce IndexError.
    except IndexError:
        print("Enter comma-separated values.")
        return

    # Si la longitud no es un número, se produce ValueError.
    except ValueError:
        print("Length must be a number.")
        return

    # Solo se aceptan ISBN de 10 o 13 caracteres.
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print("Length should be 10 or 13.")


# Descomenta esta línea para probar el programa manualmente.
# En FreeCodeCamp debe permanecer comentada para que funcionen los tests.
# main()