import os

import sys

import string


database = {}
total_file = 0
no_of_words = [0,0,0,0] # number of pos, neg, truthful, deceptive

def update_database(file_path_final, index1, index2):
    # print file_path_final
    global total_file
    global database
    global no_of_words
    total_file += 1
    punc = {',', '.', '{', '}', '(', ')', '!', '\"', '@', '#', '$', '%', '^', '&', '*', ':', ';', '/', '?', '<', '>', '=', '+'}
    stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

    curr_file = open(file_path_final, "r")

    for word in curr_file.read().split():
        # print word.lower()
        word = word.lower().strip()
        # word = word.split()
        for c in punc:
            word = word.replace(c, " ")
        word = word.strip()
        split = word.split()
        if len(split) == 1:
            # print "BC "+word
            if word in stop_words:
                continue
            if word.isdigit():
                continue
            if len(word) == 1:
                continue
            if word not in database:
                array_list = [1, 1, 1, 1]
                array_list[index1] += 1
                array_list[index2] += 1
                database[word] = array_list
            else:
                database[word][index1] += 1
                database[word][index2] += 1
            no_of_words[index1] += 1
            no_of_words[index2] += 1
        else:
            # print "AC "+word
            for splitted_word in split:
                if splitted_word in stop_words:
                    continue
                if splitted_word.isdigit():
                    continue
                if len(splitted_word) == 1:
                    continue
                if splitted_word not in database:
                    array_list = [1, 1, 1, 1]
                    array_list[index1] += 1
                    array_list[index2] += 1
                    database[splitted_word] = array_list
                else:
                    database[splitted_word][index1] += 1
                    database[splitted_word][index2] += 1
                no_of_words[index1] += 1
                no_of_words[index2] += 1
    curr_file.close()


file_path = sys.argv[1]

files_first_hierarchy = [file_or_directory for file_or_directory in os.listdir(file_path)]

# print (files_first_hierarchy)

# f2 = os.path.join(file_path, f[0])
#
# print f2

# present_working_directory = os.getcwd()
# print present_working_directory

# print os.path.isfile(f2)
number_of_positive = 0
number_of_negative = 0
number_of_truthful = 0
number_of_deceptive = 0

for files in files_first_hierarchy:
    if "positive" in files.lower():
        # print "positive"
        file_path_positive = os.path.join(file_path, files)
        # print file_path_positive
        files_second_hierarchy = os.listdir(file_path_positive)
        # print files_second_hierarchy

        for second_inner_files in files_second_hierarchy:
            if "deceptive" in second_inner_files.lower():

                #print "positive deceptive"
                file_path_pos_deceptive = os.path.join(file_path_positive, second_inner_files)
                files_third_hierarchy = os.listdir(file_path_pos_deceptive)
                for third_inner_files in files_third_hierarchy:
                    if "fold" in third_inner_files:
                        final_file_path = os.path.join(file_path_pos_deceptive, third_inner_files)
                        # here we have file names of all fold1, fold2, fold3, fold4, so iterate and call update_database function
                        for one_file_name in os.listdir(final_file_path):
                            absolute_file_path = os.path.join(final_file_path, one_file_name)
                            update_database(absolute_file_path, 0, 3)
                            number_of_deceptive += 1
                            number_of_positive += 1

            elif "truthful" in second_inner_files.lower():
                # print "positive truthful"

                file_path_pos_truthful = os.path.join(file_path_positive, second_inner_files)
                files_third_hierarchy = os.listdir(file_path_pos_truthful)
                for third_inner_files in files_third_hierarchy:
                    if "fold" in third_inner_files:
                        final_file_path = os.path.join(file_path_pos_truthful, third_inner_files)
                        # here we have file names of all fold1, fold2, fold3, fold4, so iterate and call update_database function
                        for one_file_name in os.listdir(final_file_path):
                            absolute_file_path = os.path.join(final_file_path, one_file_name)
                            update_database(absolute_file_path, 0, 2)
                            number_of_positive += 1
                            number_of_truthful += 1

    if "negative" in files.lower():
        # One level inside
        # print "negative"
        file_path_negative = os.path.join(file_path, files)
        # print file_path_negative
        files_second_hierarchy = os.listdir(file_path_negative)
        # print files_second_hierarchy

        for second_inner_files in files_second_hierarchy:
            if "deceptive" in second_inner_files.lower():
                # print "negative deceptive"

                file_path_neg_deceptive = os.path.join(file_path_negative, second_inner_files)
                files_third_hierarchy = os.listdir(file_path_neg_deceptive)
                for third_inner_files in files_third_hierarchy:
                    if "fold" in third_inner_files:
                        final_file_path = os.path.join(file_path_neg_deceptive, third_inner_files)
                        # here we have file names of all fold1, fold2, fold3, fold4, so iterate and call update_database function
                        for one_file_name in os.listdir(final_file_path):
                            absolute_file_path = os.path.join(final_file_path, one_file_name)
                            update_database(absolute_file_path, 1, 3)
                            number_of_negative += 1
                            number_of_deceptive += 1

            elif "truthful" in second_inner_files.lower():
                # print "negative truthful"

                file_path_neg_truthful = os.path.join(file_path_negative, second_inner_files)
                files_third_hierarchy = os.listdir(file_path_neg_truthful)
                for third_inner_files in files_third_hierarchy:
                    if "fold" in third_inner_files:
                        final_file_path = os.path.join(file_path_neg_truthful, third_inner_files)
                        # here we have file names of all fold1, fold2, fold3, fold4, so iterate and call update_database function
                        for one_file_name in os.listdir(final_file_path):
                            absolute_file_path = os.path.join(final_file_path, one_file_name)
                            update_database(absolute_file_path, 1, 2)
                            number_of_negative += 1
                            number_of_truthful += 1


file_out = open("nbmodel.txt", "w")
# file_out.write(str(total_file)+'\n')
file_out.write("prior_probabilty_pos_neg_tru_dec"+' '),
file_out.write(str(number_of_positive)+' '),
file_out.write(str(number_of_negative)+' '),
file_out.write(str(number_of_truthful)+' '),
file_out.write(str(number_of_deceptive)+'\n')
file_out.write("no_of_words_pos_neg_tru_dec"+' ')
file_out.write(str(no_of_words[0])+' ')
file_out.write(str(no_of_words[1])+' ')
file_out.write(str(no_of_words[2])+' ')
file_out.write(str(no_of_words[3])+'\n')


# print database
for key, value in database.items():
    file_out.write(key+" "),
    # file_out.write(str(value)+'\n')
    list = value
    file_out.write(str(list[0])+" "+str(list[1])+" "+str(list[2])+" "+str(list[3])+"\n")

file_out.close()
# print number_of_deceptive