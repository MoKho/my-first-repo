import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def digits(number):
    result = []
    length = len(str(number))
    for i in range(length, 0, -1):
        if i > 0 : 
            result.append(int(number / 10 ** (i-1)))
            number = number - result[length - i] * 10 ** (i - 1)
        else:
            result.append(int(number % 10 ** (i + 1)))
        logging.debug(str(number) + " : " + str(i) + " : " + str(len(str(number))))
    return result
'''***********************************************************'''
def left_of_number(number, digits_count):
    return int(number / ((digits(number)-digits_count) * 10))

'''***********************************************************'''

def hash_check(number, hash_c):
    ''' to check if the generated number corresponds to the given hash''' 
    hash = 0
    for d in number:
        hash = (hash * 13 + int(d)) % 100000007
    logging.debug(str(hash) + "\n" + str(hash_c))
    if hash == hash_c:
        return True
    else:
        return False
'''***********************************************************'''
def is_prime(number):
    ''' to check if the number is prime or not'''
    for i in range(2, 1 + round(number/2)):
        if(number % i == 0):
            return False
    return True
'''***********************************************************'''
def seprate(number, desired_digits):
    


'''def chain2list(chain, digits_count):
    result = []
    for i in range(1, digits(chain)):
        if i % digits_count == 0:
            result.append(chain)
'''
        



#print(hash_check("0000233331793979193911399793199139313339119333773", 34475206))
for i in range(10, 35000, 9737):
    print(i, " : ", digits(i))
'''***********************************************************'''

#def prime_maker(digits_count):
 #   while()
'''***********************************************************'''
    

