import timeit

#A simple version of the logic behind integer multiplication
#Author: Felipe Baz Mitsuishi
def integer_multiply(X, Y):
    y_list = [int(i) for i in str(Y)]
    y_list.reverse()
    resultado = 0
    for index, digit in enumerate(y_list): 
        resultado += (X * digit) * (10**index)
    return resultado


#A Karatsuba Multiplication
#Author: Felipe Baz Mitsuishi
def karatsuba_multiplication(X, Y):
    #Setup Step:
    _X = [(i) for i in str(X)]
    _Y = [(i) for i in str(Y)]

    a = ""
    b = ""
    c = ""
    d = ""

    for index, digit in enumerate(_X):
        if index < len(_X)/2:
            a += _X[index]
        else:
            b += _X[index]
    for index, digit in enumerate(_Y):
        if index < len(_Y)/2:
            c += _Y[index]
        else:
            d += _Y[index]
    
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    #First Step:
    ac = a * c
    #Second Step:
    bd = b * d
    #third Step:
    third_step = (a+b)*(c+d)
    #fourth Step:
    fourth_step = third_step - bd - ac
    #Fifth Step
    fifth_step = ac* (10 ** 4 ) + bd + fourth_step * (10 ** 2)

    return fifth_step


# A Karatsuba Multiplication Using Recursion
# Code obtained in <"https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/">
# Modify by Felipe Baz Mitsuishi
def karatsuba_recursion_multiplication(x, y):
    """
    A Karatsuba Multiplication Using Recursion
    Code obtained in <"https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/">
    Modify by Felipe Baz Mitsuishi

    Parameters:
    x (int): It is the first number of the multiplication
    y (int): It is the second number of the multiplication

    Returns:
    karatsuba_recursion_multiplication(x, y): The result of multiplying the two numbers (x and y)
    """
	# Base case of recursion
    if len(str(x)) == 1 or len(str(y)) == 1:
        # The Base Case, is an simple multiplication of 2 simple numbers
	    return x * y
    # Recursive case
    else:
        n = max(len(str(x)),len(str(y)))
        # Use whole Division to return an int
        n_divide_by_2 = n // 2
        # Use whole Division to return an int
        a = x // 10 ** (n_divide_by_2)
        # Use the rest to get the other part of the number
        b = x % 10 ** (n_divide_by_2)
        # Use whole Division to return an int
        c = y // 10 ** (n_divide_by_2)
        # Use the rest to get the other part of the number
        d = y % 10 ** (n_divide_by_2)
		
        # Recursive call
        ac = karatsuba_recursion_multiplication(a, c)
        # Recursive call
        bd = karatsuba_recursion_multiplication(b, d)
        # Recursive call
        ad_plus_bc = karatsuba_recursion_multiplication(a + b, c + d) - ac - bd
        
        # this little trick, writing n as 2 * n_divide_by_2 takes care of both even and odd n
        prod = ac * 10 ** (2 * n_divide_by_2) + (ad_plus_bc * 10 ** n_divide_by_2) + bd

        return prod


if __name__ == '__main__':
    print("-+-"*30)
    start = timeit.timeit()
    integer_multiply_response = integer_multiply(5678, 1234)
    end = timeit.timeit()
    print(f'Response of Integer Multiply: {integer_multiply_response}')
    print(f'Elapsed time of Integer Multiply: {end - start}')
    print("-+-"*30)
    start = timeit.timeit()
    karatsuba_multiplication_response = karatsuba_multiplication(5678,1234)
    end = timeit.timeit()
    print(f'Response of Karatsuba Multiply: {karatsuba_multiplication_response}')
    print(f'Elapsed time of Karatsuba Multiply: {end - start}')
    print("-+-"*30)
    start = timeit.timeit()
    karatsuba_recursive_multiplication_response = karatsuba_recursion_multiplication(5678,1234)
    end = timeit.timeit()
    print(f'Response of Karatsuba Recursive Multiply: {karatsuba_recursive_multiplication_response}')
    print(f'Elapsed time of Karatsuba Recursive Multiply: {end - start}')
    print("-+-"*30)
