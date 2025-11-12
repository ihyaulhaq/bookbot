def get_num_words(string):  
  count = len(string.split())
  return f"Found {count} total words"

def get_num_chars(string):
  char_dist = {}  
  for char in string.lower():    
    if char in char_dist:      
      char_dist[char] += 1      
    else:      
      char_dist[char] = 1        
  return char_dist

def sort_on(items):
    return items['num']

def sortedResult(items):
  sorted_list = []    
  
  for char, num in items.items():
    {"char": "b", "num": 4868}
    tmp = {"char": char , "num": num}
    sorted_list.append(tmp)
  
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list
  