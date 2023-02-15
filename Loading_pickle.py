import pickle

positional_index = open('D:/College/SEMESTER 6/IR/CSE508_Winter2023_A1_104/Positional_Index_File', 'rb')     
word_dict = pickle.load(positional_index)
for words in word_dict:
    print(words, '=>', word_dict[words])
positional_index.close()