alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
,"q","r","s","t","u","v","w","x","y","z"]

def decode(input_word, input_key):
    li_input_word = list(input_word)
    output_word = []
    i = 0
    while i < len(input_word):
        j = 0
        while j < len(alphabet):
            if (str(li_input_word[i]) == str(alphabet[j])):
                new_index = j + input_key
                if new_index > 25 or new_index < 0:
                    new_index = new_index % 26
                output_word.append(alphabet[new_index])
            j += 1    
        if (str(li_input_word[i]) == " "):
            output_word.append(" ")
        i += 1
    str_input_word = li_into_str(output_word)    
    return str_input_word

def li_into_str(element):
    output_li_into_str = ''.join(list(element))
    return output_li_into_str

word = str(input("word : "))
key = int(input("key : "))

print(decode(word, key))
