
var = "d:\College\SEMESTER 6\IR\CSE508_Winter2023_A1_104\CSE508_Winter2023_Dataset\cranfield"

for i in range(1400):
    filenum = i+1
    filename= ""
    if(filenum < 10):
        filename = var + "000" + str(filenum)
    elif(filenum<100):
        filename = var + "00" + str(filenum)
    elif(filenum<1000):
        filename = var + "0" + str(filenum)
    else:
        filename = var + str(filenum)
    file_open = open(filename, "r")
    text = file_open.readlines()
    text_len = len(text)
    title_start = 0
    title_end = 0
    text_start = 0
    text_end = 0
    for it in range(text_len):
        # print(it)
        # print(text[it])
        if(text[it] == "<TITLE>\n"):
            title_start = it
        if(text[it] == "</TITLE>\n"):
            title_end=it    
        if(text[it] == "<TEXT>\n"):
            text_start = it
        if(text[it] == "</TEXT>\n"):
            text_end=it

    title=""
    for i2 in range(title_start + 1, title_end):
        strip_text = text[i2].strip()
        title = title + strip_text

    text_content = ""
    for i3 in range(text_start + 1, text_end):
        strip_text = text[i3].strip()
        text_content = text_content + strip_text
        
    final_content = title + " " + text_content
    
    file_open.close()
    
       
    file_open = open(filename, "w")
    file_open.write(final_content)
    file_open.close()

    