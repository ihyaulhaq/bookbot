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
  
  words_num = get_num_words(get_book_text(book_path))
  char_num = get_num_chars(get_book_text(book_path))
  result = sortedResult(get_num_chars(get_book_text(book_path)))
  
  # print_result(get_num_chars(get_book_text("./books/frankenstein.txt")))
  
  
  print("============ BOOKBOT ============\n")
  print("Analyzing book found at books/frankenstein.txt...\n")
  print("----------- Word Count ----------\n")
  print(words_num)
  print("----------- Character Count ----------\n")
  for x in result:
    print(f"{x['char']}: {x['num']}")
  print("============ END ============\n")
  
