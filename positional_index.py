import os
from natsort import natsorted
import pickle

var = "D:/College/SEMESTER 6/IR/CSE508_Winter2023_A1_104/Processed_Files"
file_names = natsorted(os.listdir(var))

word_dict = {}

for i in range(len(file_names)):
    read_filename = var + "/" + file_names[i]
    final_words_array = []
    
    with open(read_filename, 'r') as filehandler:
        for line_item in filehandler:
            curr_item = line_item[:-1]
            final_words_array.append(curr_item)
    
    for j in range(len(final_words_array)):
        if final_words_array[j] not in word_dict:
            word_dict[final_words_array[j]] = []
            word_dict[final_words_array[j]].append(1)    
            word_dict[final_words_array[j]].append({})
            word_dict[final_words_array[j]][1][i+1] = [j+1]
        else:
            if( (i+1) in word_dict[final_words_array[j]][1] ):
                word_dict[final_words_array[j]][1][i+1].append(j+1)
            else:
                word_dict[final_words_array[j]][0] = word_dict[final_words_array[j]][0] + 1
                word_dict[final_words_array[j]][1][i+1] = [j+1]
                
# print(len(word_dict))
# print(word_dict)

positional_index = open('D:/College/SEMESTER 6/IR/CSE508_Winter2023_A1_104/Positional_Index_File', 'ab')
pickle.dump(word_dict, positional_index)
positional_index.close()


       