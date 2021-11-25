def merge_sort(lista):
    if(len(lista) > 1):

        # Calculates the median index of the matrix
        mid_index = len(lista)//2

        # Divide the list into two equal-sized parts
        left_half = lista[:mid_index]
        right_half = lista[mid_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lista[k]=left_half[i]
                i += 1
            else:
                lista[k]=right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k]=left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k]=right_half[j]
            j += 1
            k += 1


if __name__ == '__main__':
    lista = [2,34,123,4534,7647574,1,2,-1,2.4]
    print('-+-'*30)
    print('Dry Run = False')
    print(f'lista Antes: {lista}')
    merge_sort(lista)
    print(f'lista Depois: {lista}')
    print(f'lista: {lista}')
