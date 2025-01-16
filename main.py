def word_count(book):
    words = book.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)

main()
    