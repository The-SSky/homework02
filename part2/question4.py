def is_armstrong_for_b8(num: int):
    """
    число равно изначальному
    """
    converted = int(oct(num)[2:])
    digits = [int(d) for d in str(oct(num))[2:]]
    power = len(str(oct(num))[2:])
    s = sum(d ** power for d in digits)
    if s == num: return True
    return False

def is_armstrong_for_b8_converted(num: int):
    """
    число равно конвертированному в base8
    вычисления как в примере - в десятичной системе счисления
    """
    converted = int(oct(num)[2:])
    digits = [int(d) for d in str(oct(num))[2:]]
    power = len(str(oct(num))[2:])
    s = sum(d ** power for d in digits)
    if s == converted: return True
    return False

if __name__ == "__main__":
    for n in range(1, 999):
        if is_armstrong_for_b8(n): 
            print(f'{n}, в восьмеричной - {oct(n)[2:]}')
            continue
        if is_armstrong_for_b8_converted(n):
            print(f'{n}, конвертированное число, число армстронга в десятичной {oct(n)[2:]}')
