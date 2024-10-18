def bubbleSort(list_to_be_sorted):
    for i in range(0,len(list_to_be_sorted)):
        for j in range(i, len(list_to_be_sorted)):
            if (list_to_be_sorted[i] >= list_to_be_sorted[j]):
                temp = list_to_be_sorted[i]
                list_to_be_sorted[i] = list_to_be_sorted[j]
                list_to_be_sorted[j] = temp
    return list_to_be_sorted


if __name__ == '__main__':
    list_to_be_sorted = [3, 90, 1, 34, 2, 89, 5, 8]
    sorted_list = bubbleSort(list_to_be_sorted)
    print("Sorted List by Bubble sort ", sorted_list)