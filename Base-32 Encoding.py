import logging
import binascii
import string
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
mystring = string.ascii_uppercase[:27] + string.digits
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
    mybytes = bytes(source_string,'utf-8')
    logging.debug(str(mybytes))
    converted_string = bin(int.from_bytes(mybytes,'big'))
    logging.debug(mybytes)
    logging.debug("int.from_bytes(source_string.encode(),'big')  :  " + str(int.from_bytes(source_string.encode(),'big')))
    logging.debug(str(converted_string))
    return converted_string
def bytes_to_5bits(source_bytes):
    result = ""
    for i, x in enumerate(source_bytes):
        if i < 2 :
            continue
        if (i-1) % 5 == 0:
            result = "".join(result+str(x)+" ")
            logging.debug(result)
        else:
            result = "".join(result+str(x))
            logging.debug(result)
    logging.debug(result)
    return result

def bits_to_encode32(source_bytes):
    result = ""
    



    



bytes_to_5bits(convert_to_bytes(padding5("John")))