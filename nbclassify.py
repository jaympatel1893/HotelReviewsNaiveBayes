import os

import sys
import math

file_path = sys.argv[1]

file_in = open("nbmodel.txt", "r")
a = 0

model = {}

for f in file_in:
    temp_string = f.split()

    list = []
    for i in range(len(temp_string)):
        if i > 0:
            list.append(int(temp_string[i]))
    model[temp_string[0]] = list

    #model[temp_string[0]]
prior_probabilty_pos_neg_tru_dec = model["prior_probabilty_pos_neg_tru_dec"]
no_of_words_pos_neg_tru_dec = model["no_of_words_pos_neg_tru_dec"]
del model["prior_probabilty_pos_neg_tru_dec"]
del model["no_of_words_pos_neg_tru_dec"]
# print type(model)
# print len(model)
file_in.close()

# for key, value in model.items():
#      print key,
#      list = value
#      print list

pos_deno = no_of_words_pos_neg_tru_dec[0] + len(model)
neg_deno = no_of_words_pos_neg_tru_dec[1] + len(model)
tru_deno = no_of_words_pos_neg_tru_dec[2] + len(model)
dec_deno = no_of_words_pos_neg_tru_dec[3] + len(model)
file_out = open("nboutput.txt", "w")
for dirName, subdirList, fileList in os.walk(file_path):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        if ".txt" in fname:
            if "README" not in fname:

                chances_of_pos = 0
                chances_of_neg = 0
                chances_of_tru = 0
                chances_of_dec = 0

                absolute_file_path =  os.path.join(dirName, fname)
                file_obj = open(absolute_file_path,"r")
                punc = {',', '.', '{', '}', '(', ')', '!', '\"', '@', '#', '$', '%', '^', '&', '*', ':', ';', '/', '?', '<', '>', '=', '+'}
                stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
                for word in file_obj.read().split():
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
                        if word not in model:
                            continue
                        else:
                            chances_of_pos += math.log10(model[word][0]) - math.log10(pos_deno)
                            chances_of_neg += math.log10(model[word][1]) - math.log10(neg_deno)
                            chances_of_tru += math.log10(model[word][2]) - math.log10(tru_deno)
                            chances_of_dec += math.log10(model[word][3]) - math.log10(dec_deno)

                    else:
                        # print "AC "+word
                        for splitted_word in split:
                            if splitted_word in stop_words:
                                continue
                            if splitted_word.isdigit():
                                continue
                            if len(splitted_word) == 1:
                                continue
                            if splitted_word not in model:
                                continue
                            else:
                                chances_of_pos += math.log10(model[splitted_word][0]) - math.log10(pos_deno)
                                chances_of_neg += math.log10(model[splitted_word][1]) - math.log10(neg_deno)
                                chances_of_tru += math.log10(model[splitted_word][2]) - math.log10(tru_deno)
                                chances_of_dec += math.log10(model[splitted_word][3]) - math.log10(dec_deno)
                file_obj.close()
                first_class = ""
                second_class = ""
                if chances_of_pos > chances_of_neg:
                    second_class += "positive"
                else:
                    second_class += "negative"

                if chances_of_tru > chances_of_dec:
                    first_class += "truthful"
                else:
                    first_class += "deceptive"

                file_out.write(first_class+" ")
                file_out.write(second_class+" ")
                file_out.write(fname+"\n")
                # print first_class + " " + second_class + " " + absolute_file_path

file_out.close()

















