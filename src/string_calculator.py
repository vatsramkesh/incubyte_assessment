from src.exceptions import InvalidInputException


def add(input_string: str) -> int:
    """
    :param input_string: string of numbers to be added
    :return: Calculated the sum of input number
    """
    # If the input string is empty, return 0
    result = 0
    if not input_string:
        return result

    if input_string.startswith("//"):
        delimiter_end_index = input_string.find("\n")
        delimiter = input_string[2:delimiter_end_index]
        input_string = input_string[delimiter_end_index + 1 :]

        # Replace all instances of the delimiter with commas
        input_string = input_string.replace(delimiter, ",")

    # Replace \n with comma
    input_string = input_string.replace("\n", ",")

    negative_numbers = []
    # Split the input string by commas and iterate over splitted list and calculate sum
    for num in input_string.split(","):
        # If condition to handle , at the end of input string
        if num:
            if int(num) < 0:
                negative_numbers.append(num)
            else:
                # Since input is a string, so converting individual element to int
                result += int(num)

    if negative_numbers:
        raise InvalidInputException(
            f"negative numbers not allowed {', '.join(negative_numbers)}"
        )
    return result
