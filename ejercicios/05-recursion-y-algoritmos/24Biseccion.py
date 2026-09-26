def square_root_bisection(numero,margen = 1e-5,numero_max = 150):

  if numero < 0:
   raise ValueError("Square root of negative number is not defined in real numbers")

  if numero == 0 or numero == 1:
    print (f"The square root of {numero} is {numero}")
    return numero

  low = 0
  high = numero

  if numero < 1:
    high = 1
  
  for n in range(numero_max):
   mid = (low + high) / 2
    
   if mid * mid > numero:
        high = mid
   elif mid * mid < numero:
        low = mid
   else:
        print(f"The square root of {numero} is approximately {mid}")
        return mid 

   if high - low <= margen:
    print(f"The square root of {numero} is approximately {mid}")
    return mid

  print(f"Failed to converge within {numero_max} iterations")
  