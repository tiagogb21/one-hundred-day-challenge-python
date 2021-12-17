# Exercicio 1:

# Escreva um programa que retorne uma lista com os valores numericos de 1 a N, mas com as seguintes excecoes:

# Numeros divisiveis por 3 deve aparecer como 'Fizz' ao inves do numero;

# Numeros divisiveis por 5 devem aparecer como 'Buzz' ao inves do numero;

# Numeros divisiveis por 3 e 5 devem aparecer como 'FizzBuzz' ao inves do numero';

def fizz_buzz(n):
    store_result = [];
    for index in range(1, n):
        divisible_by_three = index % 3 == 0;
        divisible_by_five = index % 5 == 0;
        if (divisible_by_three and divisible_by_five):
            store_result.append('FizzBuzz')
        elif (divisible_by_three):
            store_result.append('Fizz')
        elif (divisible_by_five):
            store_result.append('Buzz')
        else:
            store_result.append(index)
    return store_result
    
print(fizz_buzz(30))
