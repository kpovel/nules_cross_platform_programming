import re


def read_first_sentence(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            first_sentence = re.split(r"[.!?]", text)[0]
            return first_sentence
    except FileNotFoundError:
        print("File not found")
        return None
    except IOError:
        print("IO error")
        return None


def clean_words(sentence):
    return re.findall(r"\b\w+\b", sentence, re.UNICODE)


def custom_sort(arr):
    ukrainian_alphabet = "абвгґдеєжзийіїклмнопрстуфхцчшщьюя"

    def is_ukrainian(word):
        first_char = word.lower()[0]
        return first_char in ukrainian_alphabet

    def sort_key(word):
        if is_ukrainian(word):
            return (0, word.lower())
        else:
            return (1, word.lower())

    return sorted(arr, key=sort_key)


filename = "input"
first_sentence = read_first_sentence(filename)

if first_sentence is not None:
    print("Перше речення:", first_sentence)

    words = clean_words(first_sentence)
    print("\nСлова у тексті:", words)

    sorted_words = custom_sort(words)

    print("Відсортовані слова:", sorted_words)

    print(f"\nКількість слів: {len(words)}")
