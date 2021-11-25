def bubble_sort(lista, dry_run = True):
    # Get the lenght about the list
    tam = len(lista)
    # Percorrer todos os elementos da matriz, using index starting with 0
    for i in range(tam-1):
        # We can use range(n), but outer loop will repeat one time more than necessary.
        # The last i elements are already in the correct place
        for j in range(0, tam-i-1):
            # traverse the array from 0 to n-i-1, for each element in lista
            # Swap if the element found is greater
            # than the next element
            if lista[j] > lista[j + 1] :
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    if not dry_run:
        return lista

if __name__ == '__main__':
    lista = [2,34,123,4534,7647574,1,2,-1,2.4]
    print('-+-'*30)
    print('Dry Run = False')
    print(f'lista Antes: {lista}')
    bubble_sort(lista)
    print(f'lista Depois: {lista}')
    print(f'lista: {lista}')
    print('-+-'*30)

    lista = [2,34,123,4534,7647574,1,2,-1,2.4]
    print('Dry Run = True')
    print(f'lista Antes: {lista}')
    print(f'lista Depois: {bubble_sort(lista.copy(), False)}')
    print(f'lista: {lista}')

