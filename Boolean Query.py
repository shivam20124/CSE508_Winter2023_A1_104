import pickle
import copy


positional_index = open('D:/College/SEMESTER 6/IR/CSE508_Winter2023_A1_104/Positional_Index_File', 'rb')     
word_dict = pickle.load(positional_index)
# for words in word_dict:
    # print(words, '=>', word_dict[words])
positional_index.close()

def create_querry(words, operations):
  ans = ""
  for i in range(len(words)-1):
    ans += words[i]+" "+operations[i]+" "
  ans = ans+words[-1]
  return ans

def name_and(word3,file_list):
    filenames = []
    dict_for_doc1 = word_dict[word3][1]
    for key in dict_for_doc1:
        if key in file_list:
            name = "cranfield"+ "0"*(4-len(str(key)))+str
            filenames.append( name )
    return filenames

def name_or(word3,file_list):
    filelist = copy.deepcopy(file_list)
    dict_for_doc1 = word_dict[word3][1]
    for key in dict_for_doc1:
        name = "cranfield"+ "0"*(4-len(str(key)))+str
        filelist.append( name )
    return filelist

def number_and(word3, filelist):
    return len( name_and(word3, filelist) )

def number_or(word3, filelist):
    return len( name_or(word3, filelist) )


def name_and_not(word3, file_list):
    filelist = copy.deepcopy(file_list)
    dict_for_doc1 = word_dict[word3][1]
    for key in dict_for_doc1:
        filelist.remove(key)
    return filelist

def name_or_not(word3, file_list, all_files_dict):
    filelist = copy.deepcopy(file_list)
    dict_for_doc1 = word_dict[word3][3]
    for key in all_files_dict:
        if not all_files_dict[key] in dict_for_doc1:
            filelist.append(all_files_dict[key])
    return filelist




def and_num_documents(word1,word2):
    number_of_docs = 0
    dict_for_doc1 = word_dict[word1][1]
    dict_for_doc2 = word_dict[word2][1]
    for key in dict_for_doc1:
        if key in dict_for_doc2:
            number_of_docs = number_of_docs +1
    return number_of_docs

def and_name_documents(word1, word2):
    filenames = []
    dict_for_doc1 = word_dict[word1][1]
    dict_for_doc2 = word_dict[word2][1]
    for key in dict_for_doc1:
        if key in dict_for_doc2:
            if (key<10):
                doc_name = "cranfield000" + str(key)
                filenames.append(doc_name)
            elif (key<100):
                doc_name = "cranfield00" + str(key)
                filenames.append(doc_name)
            elif (key<1000):
                doc_name = "cranfield0" + str(key)
                filenames.append(doc_name)
            else:
                doc_name = "cranfield" + str(key)
                filenames.append(doc_name)
    return filenames


def or_num_documents(word1,word2):
    number_of_docs = 0
    dict_for_doc1 = word_dict[word1][1]
    dict_for_doc2 = word_dict[word2][1]
    for key in dict_for_doc1:
        number_of_docs = number_of_docs +1
    for key in dict_for_doc2:
        if key not in dict_for_doc1:
            number_of_docs = number_of_docs + 1    
    return number_of_docs

def or_name_documents(word1, word2):
    filenames = []
    dict_for_doc1 = word_dict[word1][1]
    dict_for_doc2 = word_dict[word2][1]
    for key in dict_for_doc1:
        if (key<10):
            doc_name = "cranfield000" + str(key)
            filenames.append(doc_name)
        elif (key<100):
            doc_name = "cranfield00" + str(key)
            filenames.append(doc_name)
        elif (key<1000):
            doc_name = "cranfield0" + str(key)
            filenames.append(doc_name)
        else:
            doc_name = "cranfield" + str(key)
            filenames.append(doc_name)
    for key in dict_for_doc2:
        if(key not in dict_for_doc1):
            if (key<10):
                doc_name = "cranfield000" + str(key)
                filenames.append(doc_name)
            elif (key<100):
                doc_name = "cranfield00" + str(key)
                filenames.append(doc_name)
            elif (key<1000):
                doc_name = "cranfield0" + str(key)
                filenames.append(doc_name)
            else:
                doc_name = "cranfield" + str(key)
                filenames.append(doc_name)
    return filenames

"""for comparison"""
def binary_search(arr, x):
    
    
    comparisons = 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == x:
            return comparisons
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def total_comparisons(docs, query):
    total_comps = 0
    for word in query.split():
        if word in docs:
            total_comps += binary_search(docs[word], query)
    return total_comps
def take_input():
  for i in range(int(input("Enter no of querries"))):
    seq = input("Enter input seq: ")
    operations = [x for x in input("Enter commma seperated operation:").split(',')]
    lis = preprocessing(seq)
    querry = create_querry(lis,operations)
    return lis, querry
