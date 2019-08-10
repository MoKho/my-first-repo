import logging
import binascii
import string
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
mystring = string.ascii_uppercase[:27] + string.digits[2:]
def padding5(source_string = ""):
    if len(source_string) % 5 == 4:
        logging.debug(source_string + "1")
        return source_string + "1"
    elif len(source_string) % 5 == 3:
        logging.debug(source_string + "22")
        return source_string + "22"
    elif len(source_string) % 5 == 2:
        logging.debug(source_string + "333")
        return source_string + "333"
    elif len(source_string) % 5 == 1:
        logging.debug(source_string + "4444")
        return source_string + "4444"
    else:
        logging.debug("the string needs no padding")
        return source_string
def convert_to_bytes(source_string):
    temporary_list = list(source_string)
    logging.debug("first temporary list :" + str(temporary_list))
    for i, character in enumerate(source_string):
        temporary_list[i] = str(bin(ord(character)))
        while len(temporary_list[i]) < 10:
            temporary_list[i] = "0" + temporary_list[i]
            logging.debug("adding zero to the begining : "+ str(temporary_list[i]))
        logging.debug("temporary list :" + str(i) + str(temporary_list)) 
    converted_string = "".join(temporary_list).replace("0b","")
    logging.debug(str(converted_string))
    return converted_string

def bytes_to_5bits(source_bytes):
    result = ""
    for i, x in enumerate(source_bytes):
        if i == 0 :
            result = "".join(result+str(x)+"") 
            logging.debug("if i == 0 : " + result)
            continue
        if i % 5 == 0:
            result = "".join(result + " " + str(x))
            logging.debug("if i%5 == 0 : " +result)
        else:
            result = "".join(result+str(x))
            logging.debug("else : " + result)
    logging.debug(result)
    result = result.rsplit(" ")
    logging.debug(result)
    return result

def bits_to_encode32(source_bytes):
    for i in range(len(source_bytes)):
        source_bytes[i] = mystring[int(source_bytes[i],2)]
        logging.debug(source_bytes)
        #logging.debug(str(int(source_bytes[i], 2))
        #logging.debug(str(source_bytes[i])
    logging.debug(source_bytes)
 
    

    
    



    



bits_to_encode32(bytes_to_5bits(convert_to_bytes(padding5("John"))))