import timeit
from Bubble_Sort.bubble_sort import bubble_sort
from MergeSort.merge_sort import merge_sort


if __name__ == '__main__':
    lista = [2,34,123,4534,7647574,1,2,-1,2.4]

    print("-+-"*30)
    start = timeit.timeit()
    bubble_sort(lista)
    end = timeit.timeit()
    print(f'Response of Bubble Sort: {lista}')
    print(f'Elapsed time of Bubble Sort: {end - start}')
    print("-+-"*30)

    lista = [2,34,123,4534,7647574,1,2,-1,2.4]
    start = timeit.timeit()
    merge_sort_response = merge_sort(lista)
    end = timeit.timeit()
    print(f'Response of Merge Sort: {lista}')
    print(f'Elapsed time of Merge Sort: {end - start}')
    print("-+-"*30)