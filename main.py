def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_dict = get_char_count(text)

    print(f"--- Begin report of ${book_path} ---")
    print(f"{get_word_count(text)} words found in the document")
    print("")

    for char in char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times")
    
    print("--- End of report ---")

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