import random
import string

base = 1000
tablesize = 123987123


def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m

    return int(hash_val)


if __name__ == '__main__':
    print(string.ascii_lowercase)
    letters = string.ascii_lowercase
    result = {}
    i = 0
    while True:
        word = ''.join(random.choice(letters) for i in range(15))
        hash_val = polynomial_hash(word[::-1], base, tablesize)
        if not result.get(hash_val):
            result[hash_val] = word
        else:
            print(f'{word} - {hash_val}')
            print(result.get(hash_val), f'- {hash_val}')
            print(len(result))
            break


