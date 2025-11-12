def get_num_words(string):  
  count = len(string.split())
  return f"Found {count} total words"

def get_num_chars(string):
  char_dist = {}
  count = 0
  for char in string.lower():    
    if char in char_dist:      
      char_dist[char] += 1      
    else:      
      char_dist[char] = 1
    count+=1
    
  return count, char_dist
  
  
