from stats import *

def get_book_text(filePath):
  with open(filePath) as book:
    return book.read()
  

if __name__ == '__main__':
  print(get_num_words(get_book_text("./books/frankenstein.txt")))
  
  print(get_num_chars(get_book_text("./books/frankenstein.txt")))
  
  
  