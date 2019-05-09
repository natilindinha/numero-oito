n = 0
pares = 0
primos = 0
while n < 10:
    num = int(input('digite um numero:'))
    if num % 2 == 1 or num == 2:
        primos = primos + num
    if num % 2 == 0 :
        pares = pares + num
    n = n + 1 
print('a soma dos números primos é', primos)
print('a soma dos números pares é', pares)
