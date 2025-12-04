# #### Estrutura For
for n in range(5):
    print('Olá mundo!')


# #### Exemplo de Contagem
for num in range(10):
    print(num)


# ### Exemplo - Contage de 10 a 100 de cinco em cinco
for i in range(10, 101, 5):
    print(i)


# Usuário escolhe
inicio = int(input('Informe o início: '))
fim = int(input('Informe o final: '))

for n in range(inicio, fim):
    print(n)


# Númerando com a variável do intervalo
for num in range(3):
    print(f'Pessoa {num + 1}:')
    nome = input('Informe o nome: ')
    print(f'O nome é {nome}')


# Variável acumuladora
total = 0

for _ in range(5): # 0,1,2,3,4
    numero = float(input('Informe o valor da venda: ')) # 10
    total = total + numero


print(f'A soma é {total:.2f}')
