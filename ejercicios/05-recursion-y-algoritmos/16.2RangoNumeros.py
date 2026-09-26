def range_of_numbers(start_num,end_num):
    if start_num == end_num:
        return [start_num]
    resultado = range_of_numbers(start_num + 1, end_num)
    resultado.insert(0,start_num)
    return resultado