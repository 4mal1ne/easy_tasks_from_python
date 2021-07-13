def list_for_shift() -> list:
    """
    Convert input value with 'map' function for 'shift' function argument
    :return: input: "123456789"
            output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    result = list(map(int, input("Enter the list: ")))
    return result


def shift(shifted_list: list, value_cycle_shift: int) -> list:
    """
    Function that performs a cyclic shift. The first argument passes the list to be used,
    the second argument passes the list's shift digit.
    :param shifted_list: Global list argument
    :param value_cycle_shift: Argument for entering a number to shift our list
    :return: A processed list with objects shifted in the right direction
            by a number equal to the second argument of the function.
    """
    if value_cycle_shift < 0:
        value_cycle_shift = abs(value_cycle_shift)
        for arg in range(value_cycle_shift):
            shifted_list.append(shifted_list.pop(0))
    else:
        for arg in range(value_cycle_shift):
            shifted_list.insert(0, shifted_list.pop())
    return shifted_list


print(shift(list_for_shift(), int(input("Enter step count: "))))
