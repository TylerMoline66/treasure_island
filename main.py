punc = [',','.','?','!',':',';','(',')','_','-','“','”', "'", '’']
the_big_dic = {}
counter = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0
}
final_dic = {
  1: '',
  2: '',
  3: '',
  4: '',
  5: '',
  6: ''
}


with open("treasureisland.txt", encoding="utf-8") as raw_text:

    text_list = raw_text.readlines()
    clean_list = []
    all_the_words = []
    
    # This for loop is to strip all lines of punctuation and appends just the words to clean_list
    for line in text_list:
      for word in line:
        if word in punc:
          line = line.replace(word, '')
      clean_list.append(line.strip().split())

    # This takes the list out of the list and puts all the words with length 6 or less in all the words list
    for lst in clean_list:
      for i in lst:
        i = i.lower()
        if len(i) <= 6:
          all_the_words.append(i) 

    # This adds all words with their specific lengths to corresponding key and value pairs in the big dic
    for word in all_the_words:
      if word in the_big_dic:
        the_big_dic[word] = the_big_dic[word] + 1
      else: 
        the_big_dic[word] = 1


    # This will check the length of the word in and count how many times specific word is said
    for key in the_big_dic:
      length = len(key)
      current_value = the_big_dic[key]
      
      if current_value > counter[length]:
        counter[length] = current_value
        final_dic[length] = key



print(f"The most used one letter word is: {final_dic[1]}")
print(f"The most used two letter word is: {final_dic[2]}")
print(f"The most used three letter word is: {final_dic[3]}")
print(f"The most used four letter word is: {final_dic[4]}")
print(f"The most used five letter word is: {final_dic[5]}")
print(f"The most used six letter word is: {final_dic[6]}")