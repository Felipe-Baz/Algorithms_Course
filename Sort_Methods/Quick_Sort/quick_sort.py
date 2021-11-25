def quick_sort(lista):
    quick_sort_helper(lista, 0, len(lista)-1)


def quick_sort_helper(lista, first, last):
    if first < last:

        split_point = partition(lista, first, last)

        quick_sort_helper(lista, 0, split_point-1)
        quick_sort_helper(lista, split_point+1, len(lista)-1)

def partition(lista,first,last):
    # Define pivot value
    pivot_value = lista[first]

    # Define the left_mark and right_mark
    left_mark = first+1
    right_mark = last

    # Define the control variable
    done = False

    # traverse the sublist organizing it
    while not done:

        # Set the correct Left Mark value
        while left_mark <= right_mark and lista[left_mark] <= pivot_value:
            left_mark += 1

        # Set the correct Right Mark value
        while right_mark >= left_mark and lista[right_mark] >= pivot_value:
            right_mark -= 1
        
        # if right_mark < left_mark the array was completely traveled
        if right_mark < left_mark:
            done = True
        else:
            # Swap the values in left_mark and right_mark
            aux = lista[left_mark]
            lista[left_mark] = lista[right_mark]
            lista[right_mark] = aux

    # Swap the values in first and right_mark
    aux = lista[first]
    lista[first] = lista[right_mark]
    lista[right_mark] = aux

    return right_mark