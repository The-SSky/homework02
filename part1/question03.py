def question02(string: str):
    result = -1
    tmp = -1
    for c in string:
        c = ord(c)
        if c > 47 and c < 58:
            tmp = c if c > tmp else tmp
            result = c - 47 if c - 47 > result else result
        elif c > 64 and c < 91:
            tmp = c if c > tmp else tmp
            result = c - 54 if c - 54 > result else result
        else:
            result = -1
            break
    return result if result != 1 else 2

if __name__ == '__main__':
    tested_string1 = '000'
    tested_string2 = 'ZZZZ'
    tested_string3 = '1011'
    print(f'string 1: {question02(tested_string1)}')
    print(f'string 2: {question02(tested_string2)}')
    print(f'string 3: {question02(tested_string3)}')