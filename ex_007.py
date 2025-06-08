#Calcular a soma dos primeiros numeros até N.

n = int(input('Digite um numero positivo: '))
soma = 0

for i in range(1,n+1):
    soma+=i

print(f'a soma dos numeros de 1 a {n} é igual a {soma}')


#outra opção de fazer a soma:

n = int(input('Digite um numero positivo: '))
soma = sum(range(1, n+1))
print(f'a soma dos numeros de 1 a {n} é igual a{soma}')
    