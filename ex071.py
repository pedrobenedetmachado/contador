num = (int(input('digite um numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),
       int(input('digite o ultimo numero: ')),)
print(f'você digitou os numeros: {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o numero 3 apareceu na posição {num.index(3)+1}')
else:
    print('o numero 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(n, end='  ')