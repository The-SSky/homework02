def emulate(limit):
    """
    Длина вектора равна введенному числу
    """
    result = list()
    current_number = 1
    total = 0
    while total < limit:
        for _ in range(1, current_number + 1):
            if total == limit: break
            result.append(current_number)
            total += 1
        current_number += 1
    return result

if __name__ == "__main__":
    print(emulate(12))