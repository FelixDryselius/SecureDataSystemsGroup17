import random
import math
import string

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

def create_password(no_bits_entropy, word_list, no_words):
    password_word = []
    entropy_one_word = math.log(no_words, 2)
    entropy = 0
    while entropy < no_bits_entropy:
        random_no = random.randrange(no_words)
        password_word.append(word_list[random_no])
        entropy = entropy + entropy_one_word
    return password_word

def create_char_password(no_bits_entropy):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = range(0,10)
    char_list = lower + upper + digits
    char_list_length = len(char_list)
    entropy = 0
    count = 1
    password_char = ""
    while entropy < no_bits_entropy:
        random_char = random.randrange(char_list_length)
        password_char = password_char + str(char_list[random_char])
        entropy_char = math.log(char_list_length**count, 2)
        entropy = entropy + entropy_char
        count = count + 1
    return password_char

def print_context(no_bits_entropy):
    all_words = open_file("/usr/share/dict/words")
    word_list = split_text(all_words)
    no_words = count_words(word_list)
    password_word_list = create_password(no_bits_entropy, word_list, no_words)
    password_word = ' '.join(password_word_list)
    password_char = create_char_password(no_bits_entropy)
    print "For the entropy " + str(no_bits_entropy) + " , I suggest the passwords"
    print password_word
    print "or"
    print password_char

no_bits_entropy = 60
print_context(no_bits_entropy)

