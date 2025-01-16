def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(get_word_count(text))

def get_word_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as text:
        return text.read()


main()