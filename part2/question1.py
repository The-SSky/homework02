def find_extremum_indexes(vector:list):
    """
    возвращает индексы экстремумов в массиве-векторе
    """
    if len(vector) < 3: return None
    result = list()
    
    # обходим вектор, ищем значение слева и справа, сравниваем с текущим. 
    # по-моему в стандартной библиотеке бесконечностей нет
    # поэтому использована хитрая система ифов
    for ind in range(len(vector)):
        left = ind - 1 if ind - 1 >= 0 else None
        right = ind + 1 if ind + 1 < len(vector) else None
        if not left: 
            if vector[ind] >= vector[right]: result.append(ind)
            continue
        if not right: 
            if vector[ind] >= vector[left]: result.append(ind)
            continue
        if vector[left] <= vector[ind] >= vector[right]:
            result.append(ind)
    return result

def find_puddle_volume(vector:list):
    """
    
    """
    extremums = find_extremum_indexes(vector)
    if len(extremums) < 2: return -1

    volume = 0
    # если у нас 3 экстремума, значит должно быть 2 промежутка(пары)
    # между которыми мы будем искать объем
    pairs = [(extremums[i], extremums[i+1]) for i in range(len(extremums)-1)]
    for pair in pairs:
        minimal_extremum = min(vector[pair[0]], vector[pair[1]])
        # формируем срез на основе промежутков
        for elem in vector[pair[0] + 1:pair[1]]:
            volume += minimal_extremum - elem
    return volume


if __name__ == "__main__":
    tested_vector = [2, 5, 1, 2, 3, 4, 7, 7, 6]
    print(find_puddle_volume([5, 1, 4, 1, 4]))
    print(find_puddle_volume([2, 5, 1, 2, 3, 4, 7, 7, 6]))