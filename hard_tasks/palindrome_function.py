def max_palindrome_function(first_palindrome_val: int, second_palindrome_val: int, max_palindrome_list=[]) -> list:
    """
    A function that takes two numbers and identifies the maximal palindrome number from the sum of these two numbers
    :param first_palindrome_val: First user input value
    :param second_palindrome_val: Second user input value
    :param max_palindrome_list: Empty list for append result
    :return: Returns the maximum value from the list.
    """
    if first_palindrome_val > 100 and second_palindrome_val > 100:
        for first_val in range(1000, first_palindrome_val, -1):
            for second_val in range(1000, second_palindrome_val, -1):
                sum_arguments_result = str(first_val * second_val)
                palindrome_list = sum_arguments_result[::-1]
                if sum_arguments_result == palindrome_list:
                    palindrome_result = sum_arguments_result
                    max_palindrome_list.append(palindrome_result)
        max_palindrome_result = max(max_palindrome_list)
        print(f'The number {max_palindrome_result} is the largest possible palindrome')
        return max_palindrome_result
    else:
        print(f"Sorry, but the number must be greater than 100, your number: {first_palindrome_val}")


print(max_palindrome_function(int(input()), int(input())))
