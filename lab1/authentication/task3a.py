import random
import math

def open_file(anyfile):
    text_open = open(anyfile, "r")
    all_words = text_open.read()
    return all_words

def split_text(words):
    word_list = words.split()
    return word_list

def count_words(word_list):
    no_words=len(word_list)
    return no_words

def create_password(no_words, word_list, no_words_in_password):
    password = []
    for i in range(no_words_in_password):
        random_no = random.randrange(no_words)
        password.append(word_list[random_no])
    return password
    
def count_random_char(entropy_password):
    random_char = entropy_password/math.log(62, 2)
    return random_char

def print_context(no_words_in_password):
    all_words = open_file("/usr/share/dict/words")
    word_list = split_text(all_words)
    no_words = count_words(word_list)
    password_list = create_password(no_words, word_list, no_words_in_password)
    password = ' '.join(password_list)
    entropy_password = math.log(no_words, 2)*no_words_in_password
    no_random_char = count_random_char(entropy_password)
    print password
    print str(no_words_in_password) + " RANDOM words from word list of " + str(no_words) + " words"
    print "Entropy: " + str(("%.2f" % entropy_password))
    print "You need " + str(("%.2f" % no_random_char)) + " characters in [a-zA-Z0-9] to get the same entropy."
    
    
no_words_in_password = 4
print_context(no_words_in_password)
