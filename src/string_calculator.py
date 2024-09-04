

def add(input_string: str) -> int:
    # If the input string is empty, return 0
    result = 0
    if not input_string:
        return result
    # Replacing \n with comma
    input_string = input_string.replace("\n", ',')

    # Split the input string by commas and iterate over splitted list and calculate sum
    for num in input_string.split(','):
        # If condition to handle , at the end of input string
        if num:
            # Since input is a string, so converting individual element to int
            result += int(num)
    
    return result

