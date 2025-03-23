from stats import get_num_words
from stats import get_book_text
from stats import get_char_count
import sys


try:
    book_path_sysarg = sys.argv[1]
except Exception as inst:
    print(f"{inst} | Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = book_path_sysarg
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_char = get_char_count(text)
    print_report(book_path, num_words, count_char)



def print_report(book_path,num_words,count_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found {book_path}...")  
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    filtered_counts = {k: v for k, v in count_char.items() if k.isalpha()}
    
    sorted_counts = sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("============= END ===============")
    

main()
