import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def sum_divisors(number):
    x = 0
    for i in range(1, number):
        if number % i == 0:
            x =+ i
    #logging.debug("for " + str(number) + " : " + str(result))
    return x
finded = False
i = 0
j = 0
number = input("please input a number to find amicables below it: ")

for i in range(int(number), 219, -1):
    logging.debug("i : " + str(i) + "   j : " + str(j))
    if finded:
        break
    for j in range(int(number), 283, -1):
        if finded:
            break
        #logging.debug("i : " + str(i) + "   j : " + str(j))
        if sum_divisors(i) == j and sum_divisors(j) == i and i!=j:
            print("eureka : ", i, " and ", j)
            finded = True


