def factorial(factorial_val: int, factorial_val_start=1) -> int:
    """
    A function that takes a number and calculates its factorial.
    :param factorial_val: input argument for start range and calculate factorial
    :param factorial_val_start: start argument factorial
    :return: factorial value
    """
    for arg in range(2, factorial_val + 1):
        factorial_val_start *= arg
    return factorial_val_start


print(factorial(int(input())))
