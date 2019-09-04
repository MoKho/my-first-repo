import itertools
fibo1 = 0
fibo2 = 1
desired_digits = 500
for i in itertools.count():
    if len(str(fibo2)) == desired_digits:
        break
    fibo1 , fibo2 = fibo2, fibo1 + fibo2
print("the index is : ", i+1)


    