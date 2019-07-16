import string

abc_list = list(string.ascii_lowercase)
upper_abc_list = list(string.ascii_uppercase)

def decode(input_word, input_key):
    li_input_word = list(input_word)
    output_word = []
    i = 0

    # goes through the word/sentence
    while i < len(input_word):
        # determine the alphabet we are working with
        if (input_word[i] in abc_list):
            alphabet = abc_list
            character = True
        elif (input_word[i] in upper_abc_list):
            alphabet = upper_abc_list
            character = True
        else:
            character = False # the character is not a letter

        # check the corresponding letter
        j = 0
        while j < len(abc_list):
            if (str(li_input_word[i]) == str(alphabet[j])):
                new_index = j + input_key
                if new_index > 25 or new_index < 0:
                    new_index = new_index % 26
                output_word.append(alphabet[new_index])
            j += 1
        if character == False:
            if (str(li_input_word[i]) == " "):
                output_word.append(" ")
            else:
                output_word.append(li_input_word[i])
        i += 1
    str_input_word = li_into_str(output_word)
    return str_input_word

def li_into_str(element):
    output_li_into_str = ''.join(list(element))
    return output_li_into_str

word = str(input("word : "))
key = int(input("key : "))

print(decode(word, key))
