def hurdle_race(hurdle_arr, max_height):
    max_hurdle = max(hurdle_arr)
    var = max_hurdle - max_height
    return f" Dan must drink {var} doses"


array = list()
while len(array) < 5:
    val_to_arr = int(input('Enter Value: '))
    array.append(val_to_arr)
max_height = int(input('Height in units: '))
print(hurdle_race(array, max_height))
