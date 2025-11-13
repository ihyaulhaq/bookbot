from stats import *
import sys

def get_book_text(filePath):
  with open(filePath) as book:
    return book.read()
  



if __name__ == '__main__':
  
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  


  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  
  words_num = get_num_words(book_text)
  char_num = get_num_chars(book_text)
  result = sortedResult(char_num)
  
  # print_result(get_num_chars(get_book_text("./books/frankenstein.txt")))
  
  
  print("============ BOOKBOT ============\n")
  print(f"Analyzing book found at {book_path}...\n")
  print("----------- Word Count ----------\n")
  print(words_num)
  print("----------- Character Count ----------\n")
  for x in result:
    print(f"{x['char']}: {x['num']}")
  print("============ END ============\n")
  
