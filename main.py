from stats import count_words
from stats import count_chars
from stats import sort_chars

def main():
    char_count = {}
    char_sort = []
    book_path = "./books/frankenstein.txt"
    file_content = read_file(book_path)
    #word_count = count_words(file_content)
    #char_count = count_chars(file_content)
    #sorted_output = sort_chars(count_chars(file_content))
    clean_report(book_path, count_words(file_content), sort_chars(count_chars(file_content)))
    #char_sort = sort_chars(count_chars(file_content))
    #print(f"{word_count} words found in the document")
    #print(f"{char_count} characters found in the document")
    #print(f"{char_sort} sorted characters found in the document")


def read_file(path):
    with open(path) as f:
        return f.read()


def clean_report(path, count, dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for dict in dicts:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()