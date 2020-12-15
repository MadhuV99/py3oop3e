# letter_frequencies.py
from collections import defaultdict
from collections import Counter
import string

def letter_frequency(sentence):
    # frequencies = {}
    frequencies = defaultdict(int)
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])
d = defaultdict(tuple_counter)

CHARACTERS = list(string.ascii_letters) + [" "]
def list_letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter,frequencies[index][1]+1)
    return frequencies


def main():
    # a_sentance = 'The lazy dog'
    # print(letter_frequency(a_sentance))

    # d = defaultdict(tuple_counter) 
    # d['a'][1].append("hello")
    # d['b'][1].append('world')
    # print(d)

    # responses = [
    #             "vanilla",
    #             "chocolate",
    #             "vanilla",
    #             "vanilla",
    #             "caramel",
    #             "strawberry",
    #             "vanilla"
    #             ]
    # print("The children voted for {} ice cream".format(
    # # Counter(responses).most_common(1)[0][0]
    # # Counter(responses)
    # Counter(responses).most_common()
    #         )
    # )

    a_sentance = 'The lazy dog'
    print(list_letter_frequency(a_sentance))


if __name__ == '__main__':
    main() 