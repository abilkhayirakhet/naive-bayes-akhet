from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

spams = []
hams  = []

def parse_input_dataset(spams, hams, filename):
    f = open(filename, 'r', encoding="utf8")
    for line in f:
        if line[0] == 's':
            spams.append(line[4:])
        else:
            hams.append(line[3:])


parse_input_dataset(spams, hams, 'SMSSpamCollection')
print(len(spams))
print(len(hams))

import sys
sys.exit()
