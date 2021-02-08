import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case = []

for letter in lower_case:
    upper_case.append(letter.upper())

word_list = words.words()

def encrypt(plain, key):
    encrypted_text = ''

    for char in plain:
        if char in lower_case:
            temp = lower_case.index(char)
            temp2 = (temp + key) % 26
            encrypted_text += lower_case[temp2]
        elif char in upper_case:
            temp = upper_case.index(char)
            temp2 = (temp + key) % 26
            encrypted_text += upper_case[temp2]
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encoded, key):
    decrypted_text = ''
    decrypted_text = encrypt(encoded, -key)
    return decrypted_text

def crack(message):
    #push each word to a list 
    message_list = [message]
    # new_message_list = message_list[0].split()
    # print(new_message_list)

    all_messages_decrypted = []
    testing = []

    decrypted_text = ''
    found = False

    while found == False:
            
            counter_and_array = []
            for i in range(len(lower_case)):
                all_messages_decrypted.append([decrypt(message, i)])
                
            for sample in all_messages_decrypted:
                testing.append(sample[0].split())

        
            for array in range(len(testing)):
                to_append = ''
                counter = 0
                for words in testing[array]:
                    if words in word_list:
                        counter += 1
                    to_append += f'{words} '
                count_and_string = [to_append, counter]
            
                counter_and_array.append(count_and_string)
            # print(counter_and_array)
            value = counter_and_array[0][1]
            counter = 0
            for i in range(len(counter_and_array)):
                if value < counter_and_array[i][1]:
                    counter = i 
                    value = counter_and_array[i][1]
            found = True
            return counter_and_array[counter][0]

            
    # print(all_messages_decrypted)

    # print(testing)
    return decrypted_text
# print(encrypt('aBc', 1))

# print(decrypt('Uif', 1))

code = encrypt('It was the best of times, it was the worst of times.', 3)
print(crack(code))
# print(decrypt('eqqn ecv', 2))
