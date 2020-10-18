def find_anagram(dictionary, request):
    """
    Перебираем слова в словаре, сравниваем сумму всех кодов букв запроса 
    и сумму всех кодов букв слова. 
    Если совпало, значит найдена анаграмма
    """
    request_value = sum(ord(c) for c in request)
    for word in dictionary:
        word_value = sum(ord(c) for c in word)
        if request_value == word_value:
            return word
    return -1

if __name__ == "__main__":
    dictionary = ['рыба', 'липа', 'вдали', 'жук', 'верность', 'жара']
    print(find_anagram(dictionary, "пила"))
    print(find_anagram(dictionary, "видал"))
    print(find_anagram(dictionary, "ревность"))