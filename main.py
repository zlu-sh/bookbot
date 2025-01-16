def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(get_char_count(text))

def get_word_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as text:
        return text.read()

def get_char_count(book):
    lowered_text = book.lower()
    count_dict = {}

    for char in lowered_text:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict


main()