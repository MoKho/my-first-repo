#!/usr/bin/env python3
import string
import random
import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def passwordgenerator(length = 0, upper = "y", lower = "y", digits = "y", punc = "y", whitespace = "n"):
    def password_sequence(charset = ""):
        if charset == "":
            return random.choice(string.ascii_letters + string.digits + string.punctuation + " ")
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
        if digits == "n" and upper == "n" and lower == "n" and punc == "n":
            raise "Password could not be empty."
    
    if length == "0" or int(length) > 16:
        length = random.randint(5, 16)
        #logging.debug("password length: " + str(length))
    for i in range(0, int(length)):
        if i == 0:
            password_characters = [password_sequence(characterset)]
        else:
            password_characters += password_sequence(characterset)
        #logging.debug("making passwords ===>    " + str(password_characters))
    random.shuffle(password_characters)
    #logging.debug("now the shuffled password is: " + str(password_characters))
    password = "".join(password_characters)
    
    print('\n\n\nyour password is :  <' + password, end='>\n')
    return password
x = len(sys.argv) 
if x > 7 or x < 1:
    #logging.debug("x has :  " + str(x) + "characters")
    raise "You have to input between 1 to 6 parameters."
while True:
    x = 0
    y = [8,"y","y","n","n","n","n"]
    for x in range(len(sys.argv)-1):
        y[x] = sys.argv[x+1]
        logging.debug("the " + str(x) + " of y is : " + str(y[x]))
 
   
    try:
        passwordgenerator(y[0], y[1], y[2], y[3], y[4], y[5])
    except Exception as myerror:
        print("could not make a password due to :  ", myerror)
    if input("\nyou wanna try again?(y/n)") == "n":
        break