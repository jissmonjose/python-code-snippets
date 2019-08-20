arr1 = []


def picking_numbers(array):
    global arr1
    for each in array:
        if arr1 is []:
            arr1.append(each)
        else:
            for each2 in arr1:
                var = each - each2
                if abs(var) is 1:
                    arr1.append(each)
                    break
            print('hello')
            # print(arr1)


print(picking_numbers([1, 2, 2]))
