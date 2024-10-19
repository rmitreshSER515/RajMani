def selectionSort(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted)):
        min = list_to_be_sorted[i]
        min_index = i
        for j in range(i+1, len(list_to_be_sorted)):
            if (list_to_be_sorted[j] < min):
                min = list_to_be_sorted[j]
                min_index = j
        temp = list_to_be_sorted[i]
        list_to_be_sorted[i] = list_to_be_sorted[min_index]
        list_to_be_sorted[min_index] = temp
    return list_to_be_sorted


if __name__ == '__main__':
    list_to_be_sorted = [9, 7, 1, 34, 89, 12, 0]
    sorted_list = selectionSort(list_to_be_sorted)
    print("The sorted list is", sorted_list)