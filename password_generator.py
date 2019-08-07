#!/usr/bin/env python3
import string
import random
import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def passwordgenerator(length = 0, upper = "y", lower = "y", digits = "y", punc = "y", whitespace = "n"):
    def password_sequence(charset = ""):
        if charset == "":
            return random.choice(string.printable)
        else:
            return random.choice(charset)
    password_characters = [""]
    characterset = ""
    if upper == "y":
        characterset += string.ascii_uppercase        
    if lower == "y":
        characterset += string.ascii_lowercase
    if digits == "y":
        characterset += string.digits
    if punc == "y": 
        characterset += string.punctuation
    if whitespace == "y": 
        characterset += " "
    if length == "0" or int(length) > 16:
        length = random.randint(5, 16)
        logging.debug("password length: " + str(length))
    for i in range(0, int(length)):
        if i == 0:
            password_characters = [password_sequence(characterset)]
        else:
            password_characters += password_sequence(characterset)
        logging.debug("making passwords ===>    " + str(password_characters))
    random.shuffle(password_characters)
    logging.debug("now the shuffled password is: " + str(password_characters))
    password = "".join(password_characters)
    
    print('\n\n\nyour password is :  <' + password, end='>\n')
    return password

'''
length = int(input("how many chars?( 0 for random length)   :    "))
upper = input("uppercase?(y/n)   :    ")
lower = input("lowercase?(y/n)   :    ")
digits = input("Digits?(y/n)   :    ")
punc = input("punctuations?(y/n)   :    ")
whitespace = input("whitespaces?(y/n)   :     ")
'''
#passwordgenerator(arguments[:])
passwordgenerator(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
