def reverse_arguments(func) -> object:
    """
    Function decorator. Argument -> function wrapper
    :param func: wrapper.
    :return: wrapper function.
    """

    def wrapper(*args) -> int:
        """
        A function that swaps function arguments.
        :param args: any args.
        :return: Reverse function '*args'(any) arguments
        """
        return func(*args[::-1])

    return wrapper


@reverse_arguments
def num_exponentiation(arg_1: int, arg_2: int) -> int:
    """
    The function of degree expansion. Takes any number of arguments and powers them up.
    :param arg_1: first argument(int)
    :param arg_2: second argument(int)
    :return: The result of multiplying one argument by another.
    """
    return arg_1 ** arg_2


print(num_exponentiation(4, 5))
