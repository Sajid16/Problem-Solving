def reverse_words_order_and_swap_cases(sentence):
    result_list = []
    final_sentence = ""
    sentence_to_word = sentence.split()
    sentence_to_word = list(reversed(sentence_to_word))
    reversed_sentence = (" ".join(sentence_to_word))
    sentence_to_char_list = list(reversed_sentence)
    for char in sentence_to_char_list:
        if char.isupper() == 1:
            result_list.append(char.lower())
        else:
            result_list.append(char.upper())
    for char in result_list:
        final_sentence += char
    # print(final_sentence)
    return final_sentence

sentence = str(input())
reverse_words_order_and_swap_cases(sentence)

