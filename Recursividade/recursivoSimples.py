#Potencia
def pot(n, e):
    if e == 0: return 1
    return n * pot(n, e-1)

print(pot(4,3))

#Soma até N
def sd(n):
    if n == 0: return 0
    return n + sd(n-1)

print(sd(6))


#Minimo divisivel comum
#def mdc (a, b):

#Tranformando decimal p/ binário
def dec2bin (n):
    if n == 0: return 0
    else: return n%2+10*dec2bin(n//2)

print(dec2bin(5678))



#Inverso de uma string
def inv (s):
    if s == '': return s
    else: return s[-1]+inv(s[:-1])

print('batata')


#Fibonacci
from functools import lru_cache #O que mais se usa fica na memória e mais fácil de acessar.

@lru_cache(maxsize=None) #Armazena se já foi feita a chamada, não deixando repetir.
def fib(n):
    print (n)
    if n == 1 or n==2: return 1 
    return fib(n-1) + fib(n-2)

print(fib(100))