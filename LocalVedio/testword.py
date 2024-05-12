def pig_latin(word):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'  # 注意这里不包括'y'，因为'y'的处理有例外

    # 特殊处理以'y'开头的情况，将其视作辅音
    if word[0].lower() == 'y':
        return word[1:] + word[0] + 'ay'

    # 检查单词是否以元音开头（现在包括'y'在非首位置的情况）
    if word[0].lower() in vowels:
        return word + 'way'

    # 处理以"qu"开头的特殊情况
    if word[:2].lower() == 'qu':
        return word[2:] + 'quay'

    # 非'y'的元音出现的位置，
    first_vowel_index = next((i for i, letter in enumerate(word) if letter.lower() in vowels and letter != 'y'), None)

    if first_vowel_index is not None:
        # 分割辅音
        consonant_cluster = word[:first_vowel_index]
        rest_of_word = word[first_vowel_index:]

        # 将辅音末尾并加"ay"
        return rest_of_word + consonant_cluster + 'ay'
    else:
        # 没有找到非'y'的元音，
        return word


while True:
     user_input = input("Enter an English word to translate into Pig Latin (or 'quit' to exit): ")
     if user_input.lower() == '.':
         break
     print(pig_latin(user_input))