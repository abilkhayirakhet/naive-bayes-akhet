# lab 2 Naive Bayes
# Akhet Abilkhayir


from nltk.tokenize import RegexpTokenizer
from nbcclassifier import NaiveBayes

tokenizer = RegexpTokenizer(r'\w+')
naive_bayes = NaiveBayes()

spams = []
hams  = []
spam_words = []
ham_words  = []

def parse_input_dataset(spams, hams, filename):
    lines = open(filename, 'r', encoding="utf8")
    for line in lines:
        first_word = tokenizer.tokenize(line).pop(0)
        if is_line_spam(first_word):
            spams.append(line[4:])
        else:
            hams.append(line[3:])


def is_line_spam(word):
    return word == 'spam'


parse_input_dataset(spams, hams, 'SMSSpamCollection')


for spam in spams:
    spam_words += tokenizer.tokenize(spam)

for ham in hams:
    ham_words += tokenizer.tokenize(ham)

naive_bayes.train(ham_words, spam_words)

message = ""

while message != "quit":
    message = input("Text for prediction:")
    if naive_bayes.is_ham(tokenizer.tokenize(message)):
        print("HAM")
    else:
        print("SPAM")