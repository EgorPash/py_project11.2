def capitalize_all_letters(input_string):
    """
        Converts all letters in the input string to uppercase.

        Args:
            input_string (str): The input string.

        Returns:
            str: The input string with all letters capitalized.
        """
    return input_string.upper()

# Пример использования функции:
input_string = "Пример строки с разным регистром"
result = capitalize_all_letters(input_string)
print(result)

def capitalize_first_letters(input_string):
    """
    Capitalizes the first letter of each word in the input string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    return input_string.title()

# Пример использования функции:
input_string = "пример строки с разным регистром"
result = capitalize_first_letters(input_string)
print(result)
