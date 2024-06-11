def calculate_structure_sum(list_):
    total_sum = 0
    total_len = 0

    for item in list_:
        if isinstance(item, list):
            total_sum += sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                total_sum += calculate_structure_sum(value)
                if isinstance(key, str):
                    total_len += len(key)
        elif isinstance(item, tuple):
            for dict_ in item:
                if isinstance(dict_, dict):
                    for key, value in dict_:
                        total_sum += calculate_structure_sum(value)
                        if isinstance(key, str):
                            total_len += len(key)
                for dict2 in dict_:
                    if isinstance(dict2, list):
                        for key, value in dict_.items():
                            total_sum += calculate_structure_sum(value)
                            if isinstance(key, str):
                                total_len += len(key)
        elif isinstance(item, str):
            total_len += len(item)



    return total_sum, total_len


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)