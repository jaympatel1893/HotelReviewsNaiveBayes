# Naive Bayes Classifier for Hotel Reviews

A Naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative.
### Training Data:
- A top-level directory with two sub-directories, one for positive reviews and another for negative reviews .
- Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews.
- Each of these subdirectories contains four subdirectories, called “folds”.
- Each of the folds contains 80 text files with English text (one review per file).

#### Two files:

##### nblearn.py:
The program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt

##### nblclassify.py:

The program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each file in the test data, and write the results to a text file called nboutput.txt in the following format:

label_a label_b path1    
label_a label_b path2 
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.


