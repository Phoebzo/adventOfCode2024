import pandas as pd

data = pd.read_csv('soemthing.txt', header = None)
#data = pd.read_csv('trying.txt', header = None)
print(data)

safe_unsafe_list = []

 
def safe_search(data):
    unsafe_levels_counter = 0
    unsafe_levels_counter_assend = is_assending(data, unsafe_levels_counter)
    unsafe_levels_counter_descend = is_descending(data, unsafe_levels_counter)

    if min(unsafe_levels_counter_assend, unsafe_levels_counter_descend) >= 2:
        unsafe_levels_counter_assend = is_assending(data[1:], unsafe_levels_counter +1)
        unsafe_levels_counter_descend = is_descending(data[1:], unsafe_levels_counter +1)
        if min(unsafe_levels_counter_assend, unsafe_levels_counter_descend) >= 2:
            return False
        else: 
            return True
    else:
        return True

def is_assending(data, unsafe_levels_counter):
    if len(data) > 1:
        if (int(data[0]) - int(data[1])) >= 0 or (int(data[0]) - int(data[1])) < -3:

            if len(data) > 2 :
                if ((int(data[0]) - int(data[2])) >= 0 or (int(data[0]) - int(data[2])) < -3):
                    return unsafe_levels_counter + 2
                else: 
                    unsafe_levels_counter = is_assending(data[2:], unsafe_levels_counter + 1)
            else:
                return unsafe_levels_counter + 1
        else:
            unsafe_levels_counter = is_assending(data[1:], unsafe_levels_counter)

    return unsafe_levels_counter

def is_descending(data, unsafe_levels_counter):
    if len(data) > 1:
        if (int(data[0]) - int(data[1])) <= 0 or (int(data[0]) - int(data[1])) > 3:
            
            if len(data) > 2:
                if ((int(data[0]) - int(data[2])) <= 0 or (int(data[0]) - int(data[2])) > 3):
                    return unsafe_levels_counter + 2
                else:
                    unsafe_levels_counter = is_descending(data[2:], unsafe_levels_counter + 1)
            else: 
                return unsafe_levels_counter + 1
        else:
            unsafe_levels_counter = is_descending(data[1:], unsafe_levels_counter)

    return unsafe_levels_counter


for i in range(0, len(data[0])):
    list_of_num = data[0][i].split()
    safe_unsafe_list.append(safe_search(list_of_num))

safe = safe_unsafe_list.count(True)
print(safe)