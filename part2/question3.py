def filter_out_non_roman_digits_elements(roman_list: list):
    """
    case sensitive
    """
    result = list()
    roman_digits = ('X', 'I', 'V', 'L', 'M', 'C', 'D', 'M')
    for entry in roman_list:
        if all(True if char in roman_digits else False for char in entry):
            result.append(entry)
    return result

if __name__ == "__main__":
    roman_list = ['VVV', 'VC', 'RVC', 'AWE', 'CAESAR', 'XIV']
    print(filter_out_non_roman_digits_elements(roman_list))