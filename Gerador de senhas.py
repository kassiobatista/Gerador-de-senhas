import random, string

tamanho = int(input('Digite a quantidade de caracteres da sua senha: '))

chars = string.ascii_letters + string.digits + 'Ç!@#$%&*()+_-;:><{}'

rnd = random.SystemRandom()


print(''.join(rnd.choice(chars) for i in range(tamanho)))
