data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
all_sum = 0
def calculate_structure_sum(*args):
    global all_sum
    for i in args:
        if isinstance(i, int):
            all_sum += i
        elif isinstance(i,str):
            all_sum += len(i)
        elif isinstance(i, dict):
            calculate_structure_sum(*i.items())
        else:
            calculate_structure_sum(*i)
    return all_sum
result = calculate_structure_sum(*data_structure)
print(result)