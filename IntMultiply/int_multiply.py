#A simple version of the logic behind integer multiplication
def integer_multiply(a, b):
    b_list = [int(i) for i in str(b)]
    b_list.reverse()
    resultado = 0
    for index, digit in enumerate(b_list):
        resultado += (a * digit) * (10**index)
    return resultado


if __name__ == '__main__':
    print(integer_multiply(1234, 9876))
