def task6_1 (text) :
    words = text.replace('\n',' ').split()
    distinctWords = set(word for word in words)
    return distinctWords


def task6_2(text):
    words = text.replace('\n', ' ').split()
    lines = text.split('\n')
    word_positions = {}  # dict
    position = 1
    for line in lines:
        line_words = line.split()
        for i, word in enumerate(line_words):
            if i == len(line_words) - 1:
                position_value = -position
            else:
                position_value = position
            if word in word_positions:
                word_positions[word].append(position_value)
            else:
                word_positions[word] = [position_value]
            position += 1

    return word_positions
def task6_3(text):
    dict = {}
    words = text.replace('\n', ' ').split()
    for word in words :
        if word in dict :
            dict[word] += 1
        else :
            dict[word] = 1
    return max (dict, key = dict.get)



def task6_4(word_positions):
    # Create a list to hold the words in their correct positions
    max_position = max(abs(pos) for positions in word_positions.values() for pos in positions)
    words_list = [''] * max_position

    # Place each word in the correct position in the list
    for word, positions in word_positions.items():
        for pos in positions:
            index = abs(pos) - 1
            if pos < 0:
                words_list[index] = word + '\n'
            else:
                words_list[index] = word

    # Join the list into a single string with spaces and newlines as appropriate
    result = ' '.join(words_list).replace('\n ', '\n')
    return result

    #Test case
text = ("What have I\n"
        "What have I\n"
        "What have I done to deserve this ")
    #6.1
print (task6_1(text) )
    #6.2
word_positions = task6_2(text)
print("Word       Word Position(s)")
print("===========================")
for word, positions in word_positions.items():
    print(f"{word:<10} {', '.join(map(str, positions))}")
print ("The most frequent word: ")
    #6.3
task6_3(text)
    #6.4
reconstructed_text = task6_4(word_positions)
print(reconstructed_text)