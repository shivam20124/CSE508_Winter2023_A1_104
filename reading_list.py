#This file provides with the code to read the tokenized words for further parts

var_read = "d:\College\SEMESTER 6\IR\CSE508_Winter2023_A1_104\Processed_Files\cranfield"

for i in range(1400):
    filenum = i+1
    read_filename= ""
    if(filenum < 10):
        read_filename = var_read + "000" + str(filenum)
    elif(filenum<100):
        read_filename = var_read + "00" + str(filenum)
    elif(filenum<1000):
        read_filename = var_read + "0" + str(filenum)
    else:
        read_filename = var_read + str(filenum)
    
    final_words_array = []
    
    with open(read_filename, 'r') as filehandler:
        for line_item in filehandler:
            curr_item = line_item[:-1]
            final_words_array.append(curr_item)
    
