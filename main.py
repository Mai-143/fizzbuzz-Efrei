
def fizzbuzz():
    result = []  # Stocker les résultats au lieu d'imprimer
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result  # Retourner la liste des résultats


if __name__ == '__main__':
    fizzbuzz()

