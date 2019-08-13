import logging
import binascii
import string
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
mystring = string.ascii_uppercase[:27] + string.digits[2:]
def padding5(source_string = ""):
    '''
        Padding the raw message so it has a product of five characters.
    '''
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
        #logging.debug(source_string + "55555")
        return source_string + "55555"
def convert_to_bytes(source_string):
    '''
        converting the padded raw message to 8-bits bytes, glued together
    '''
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
    #logging.debug("encoded bits are : " + str(result))
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
    #logging.debug("********* Now Decoding :" + encoded_msg + "  ************")
    temporary_list = []
    for i in encoded_msg:
        a = mystring.find(i)
        bits_count = len(str(bin(a))) - 2
        #logging.debug("bits count :" + str(bits_count) + " adding : " + str(5-bits_count) + " for character : " + i)
        temporary_list.append("0"*(5-bits_count) + str(bin(a)))
        #logging.debug(str(temporary_list) + str(a))
    encoded_msg = "".join(temporary_list).replace("0b","")
    #logging.debug(encoded_msg)
    return encoded_msg

def fivebits_to_byte(binary_msg):
    #logging.debug("the binary msg : " + binary_msg)
    result = ""
    for i, x in enumerate(binary_msg):
        if i == 0 :
            result = "".join(result+str(x)+"") 
            #logging.debug("if i == 0 : " + result)
            continue
        if i % 8 == 0:
            result = "".join(result + " " + str(x))
            #logging.debug("if i%5 == 0 : " +result)
        else:
            result = "".join(result+str(x))
            #logging.debug("else : " + result)
    #logging.debug(result)
    result = result.rsplit(" ")
    #logging.debug("the bits are : " + "".join(result))
    return "".join(result)

def binary_to_string(data):
    #logging.debug("************ now converting to string************")
    output = []
    for i in range(1, len(data)+1):
        #logging.debug("the " + str(i) + " time: ")
        if i % 8 == 0:
            #logging.debug("now doing this byte : " + str(i) + " : " + str(int(data[i-8:i],2)) + " : " + chr(int(data[i-8:i],2)))
            output.append(chr(int(data[i-8:i],2)))
    #logging.debug("the result is : " + str(output))
    output = "".join(output)
    finaloutput = output[:(len(output)-int(output[len(output)-1]))]
    
    return finaloutput

def encode32(the_string):
    return bits_to_encode32(bytes_to_5bits(convert_to_bytes(padding5(the_string))))

def decode32(the_string):
    return binary_to_string(fivebits_to_byte(encoded_to_bits(the_string)))



print(encode32("Ng Sir three"), decode32("ONUXIIDUNBZGKZJAMR2WK3DMNFXGOIDTNF2CAZDVMVWGY2LOM42DINBU"), end = " ")
print(encode32("Sir"), decode32("ONUXIIDUNBZGKZJAONUXIMRS"), end = " ")
print(encode32("blind Ng"), decode32("MJWGS3TEGU2TKNJV"))
