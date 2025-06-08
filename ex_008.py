"""
Verificador de Número Primo
---------------------------
Este script solicita ao usuário um número inteiro e informa se ele é um número primo ou não.
"""
def is_prime(n):
    if n <=1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def main():
    escolha = int(input('Digite um numero maior que 1: '))

    if is_prime(escolha):
        print(f'{escolha} é primo')
    else:
        print(f'{escolha} não é primo')

if __name__ == '__main__':
    main()


