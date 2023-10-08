# Takes a list of mixed values as input, calculates the mean of all the numbers found in the list and returns it.
def calc_mean_num_of_mixed_vals_list(vals) -> float | None:
    not_a_num_count: int = 0
    total: float = 0.0
    if not is_list(vals):
        return None
    for i in range(len(vals)):
        if is_num(vals[i]):
            total += vals[i]
        else:
            not_a_num_count += 1
    length = (len(vals) - not_a_num_count) if len(vals) != not_a_num_count else 0
    mean = (total / length) if length > 0 else None
    return mean


# Takes a list of mixed values as input and returns the maximum number of all the numbers found in the list.
def get_max_num_in_mixed_vals_list(vals) -> int | float | None:
    max_num: int | float | None = None
    if not is_list(vals):
        return None
    for i in range(len(vals)):
        if is_num(vals[i]):
            if max_num is None:
                max_num = vals[i]
            if vals[i] > max_num:
                max_num = vals[i]
    return max_num


# Takes a list of mixed values as input and returns the most common number of all the numbers found in the list.
def get_mode_num_in_mixed_vals_list(vals) -> int | float | None:
    max_count: int | float | None = None
    mode_num: int | float | None = None
    num_dict = {}
    if not is_list(vals):
        return None
    for i in range(len(vals)):
        if is_num(vals[i]):
            if vals[i] in num_dict:
                num_dict[vals[i]] += 1
            else:
                num_dict[vals[i]] = 1
    for key, value in num_dict.items():
        if max_count is None:
            max_count = value
            mode_num = key
        if value > max_count:
            max_count = value
            mode_num = key
    return mode_num


# Utilities
def is_num(val) -> bool:
    return type(val) is int or type(val) is float


def is_list(vals) -> bool:
    return type(vals) is list and len(vals) > 0
