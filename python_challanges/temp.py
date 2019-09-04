import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
def amicable_sum(num):
    divisor_sum = [0] * num
    for i in range(1, len(divisor_sum)):
        
        for j in range(i * 2, len(divisor_sum), i):
            logging.debug(" divisorsum  " + str(divisor_sum))
            divisor_sum[j] += i

	# Find all amicable pairs 
    result = 0
    for i in range(1, len(divisor_sum)):
        j = divisor_sum[i]
        if j != i and j < len(divisor_sum) and divisor_sum[j] == i:
            result += i
            #logging.debug("result : " + str(result) + "  i: " + str(i))
    return str(result)
print(amicable_sum(20))

