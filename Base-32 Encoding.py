import logging
import binascii
import string
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
mystring = string.ascii_uppercase[:27] + string.digits[2:]
def padding5(source_string = ""):
    if len(source_string) % 5 == 4:
        #logging.debug(source_string + "1")
        return source_string + "1"
    elif len(source_string) % 5 == 3:
        #logging.debug(source_string + "22")
        return source_string + "22"
    elif len(source_string) % 5 == 2:
        #logging.debug(source_string + "333")
        return source_string + "333"
    elif len(source_string) % 5 == 1:
        #logging.debug(source_string + "4444")
        return source_string + "4444"
    else:
        #logging.debug("the string needs no padding")
        return source_string
def convert_to_bytes(source_string):
    temporary_list = list(source_string)
    #logging.debug("first temporary list :" + str(temporary_list))
    for i, character in enumerate(source_string):
        temporary_list[i] = str(bin(ord(character)))
        while len(temporary_list[i]) < 10:
            temporary_list[i] = "0" + temporary_list[i]
            #logging.debug("adding zero to the begining : "+ str(temporary_list[i]))
        #logging.debug("temporary list :" + str(i) + str(temporary_list)) 
    converted_string = "".join(temporary_list).replace("0b","")
    #logging.debug(str(converted_string))
    return converted_string

def bytes_to_5bits(source_bytes):
    result = ""
    for i, x in enumerate(source_bytes):
        if i == 0 :
            result = "".join(result+str(x)+"") 
            #logging.debug("if i == 0 : " + result)
            continue
        if i % 5 == 0:
            result = "".join(result + " " + str(x))
            #logging.debug("if i%5 == 0 : " +result)
        else:
            result = "".join(result+str(x))
            #logging.debug("else : " + result)
    #logging.debug(result)
    result = result.rsplit(" ")
    #logging.debug(result)
    return result

def bits_to_encode32(source_bytes):
    for i in range(len(source_bytes)):
        source_bytes[i] = mystring[int(source_bytes[i],2)]
        #logging.debug(source_bytes)
    #logging.debug(source_bytes)
    result = ""
    result = "".join(source_bytes)
    return result
    


def encoded_to_bits(encoded_msg):
    logging.debug("********* Now Decoding ************")
    temporary_list = []
    for i in encoded_msg:
        a = mystring.find(i)
        if a < 16:              #converting the 4 digits characters to 5 digits
            temporary_list += '0' + bin(a)
        else:
            temporary_list += bin(a)
        logging.debug(str(temporary_list) + str(a))
    encoded_msg = "".join(temporary_list).replace("0b","")
    logging.debug(encoded_msg)
    return encoded_msg

def fivebits_to_byte(binary_msg):
    result = ""
    for i, x in enumerate(binary_msg):
        if i == 0 :
            result = "".join(result+str(x)+"") 
            logging.debug("if i == 0 : " + result)
            continue
        if i % 8 == 0:
            result = "".join(result + " " + str(x))
            logging.debug("if i%5 == 0 : " +result)
        else:
            result = "".join(result+str(x))
            logging.debug("else : " + result)
    logging.debug(result)
    result = result.rsplit(" ")
    logging.debug(result)
    return result

def binary_to_string(decoded_msg):
    logging.debug("************ now converting to string************")
    for i in range(len(decoded_msg)):
        decoded_msg[i] = chr(int(decoded_msg[i],2))
        logging.debug(decoded_msg)
    result = "".join(decoded_msg)
    return result

def encode32(the_string):
    return bits_to_encode32(bytes_to_5bits(convert_to_bytes(padding5(the_string))))

def decode32(the_string):
    binary_to_string(fivebits_to_byte(encoded_to_bits(the_string)))

#print(encode32("Ng Sir three"), encode32("Sir"), encode32("blind Ng"))
print(decode32("ONUXIIDUNBZGKZJAMR2WK3DMNFXGOIDTNF2CAZDVMVWGY2LOM42DINBU"))
#print(decode32("ONUXIIDUNBZGKZJAONUXIMRS"))
#print(decode32("MJWGS3TEGU2TKNJV"))


    
    

    
    



    



