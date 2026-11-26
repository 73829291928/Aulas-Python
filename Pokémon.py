import random

print('===== POKÉMON BATTLE 3.0 =====')
print('1 - Pikachu | 2 - Charmander | 3 - Squirtle | 4 - Bulbasaur')
escolha = input('Escolha seu Pokémon: ')
while escolha not in ('1', '2', '3', '4'):
    escolha = input('Opção inválida. Escolha novamente: ')

# Nome, tipo, vida, dano, golpe normal, golpe especial, evolução
pokemons = {
    '1': ('Pikachu', 'Elétrico', 100, 25, 'Choque do Trovão', 'Trovão', 'Raichu'),
    '2': ('Charmander', 'Fogo', 90, 30, 'Brasa', 'Lança-chamas', 'Charmeleon'),
    '3': ('Squirtle', 'Água', 120, 20, 'Jato de Água', 'Hidro Bomba', 'Wartortle'),
    '4': ('Bulbasaur', 'Grama', 110, 22, 'Chicote de Vinha', 'Raio Solar', 'Ivysaur')
}

nome, tipo, vida_max, ataque, golpe, especial, evolucao = pokemons[escolha]

# Calcula a vantagem de tipo

def multiplicador(a, b):
    if (a, b) in [('Fogo', 'Grama'), ('Água', 'Fogo'), ('Grama', 'Água'), ('Elétrico', 'Água')]:
        return 2
    elif (a, b) in [('Grama', 'Fogo'), ('Fogo', 'Água'), ('Água', 'Grama'), ('Elétrico', 'Grama')]:
        return 0.5
    return 1

# Mostra a barra de vida

def barra(vida, maxima):
    blocos = vida * 20 // maxima
    return '[' + '#' * blocos + '-' * (20 - blocos) + ']'

# Executa um ataque

def atacar(nome, golpe, dano, mult, especial, defesa):
    chance = 90
    if especial:
        chance = 70
        dano = dano * 1.5
    print(nome, 'usou', golpe)
    if random.randint(1, 100) > chance:
        print('O ataque errou!')
        return 0
    if random.randint(1, 100) <= 15:
        dano = dano * 2
        print('Golpe crítico!')
    dano = dano * mult
    if mult == 2:
        print('Super efetivo!')
    elif mult == 0.5:
        print('Pouco efetivo!')
    if defesa:
        dano = dano / 2
        print('A defesa reduziu o dano!')
    dano = int(dano)
    print('Dano causado:', dano)
    return dano

vitorias = 0
evoluiu = False
continuar = 's'
while continuar == 's':
    sorteio = str(random.randint(1, 4))
    while sorteio == escolha:
        sorteio = str(random.randint(1, 4))
    inimigo, tipo_c, max_c, ataque_c, golpe_c, especial_c, _ = pokemons[sorteio]
    vida = vida_max
    vida_c = max_c
    pocoes = 2
    pocoes_c = 2
    fugiu = False
    rodada = 1
    print('\n', nome, 'VS', inimigo)
    while vida > 0 and vida_c > 0 and not fugiu:
        print('\nRODADA', rodada)
        print(nome, barra(vida, vida_max), vida, '/', vida_max)
        print(inimigo, barra(vida_c, max_c), vida_c, '/', max_c)
        print('1 - Atacar | 2 - Especial | 3 - Defender')
        print('4 - Poção (', pocoes, ') | 5 - Fugir')
        acao = input('Sua ação: ')
        if acao == '5':
            fugiu = True
            break
        if acao not in ('1', '2', '3', '4'):
            print('Opção inválida!')
            continue
        if acao == '4' and (pocoes == 0 or vida == vida_max):
            print('Não é possível usar uma poção agora!')
            continue

        # O computador escolhe sua ação antes dos ataques
        sorte = random.randint(1, 100)
        if vida_c <= max_c * 0.35 and pocoes_c > 0 and sorte <= 65:
            acao_c = '4'
        elif sorte <= 45:
            acao_c = '1'
        elif sorte <= 80:
            acao_c = '2'
        else:
            acao_c = '3'

        if acao == '1' or acao == '2':
            vida_c = max(0, vida_c - atacar(nome, especial if acao == '2' else golpe, ataque, multiplicador(tipo, tipo_c), acao == '2', acao_c == '3'))
        elif acao == '3':
            print(nome, 'se defendeu!')
        elif acao == '4':
            vida = min(vida_max, vida + 30)
            pocoes -= 1
            print(nome, 'usou uma poção!')

        if vida_c > 0:
            if acao_c == '1' or acao_c == '2':
                vida = max(0, vida - atacar(inimigo, especial_c if acao_c == '2' else golpe_c, ataque_c, multiplicador(tipo_c, tipo), acao_c == '2', acao == '3'))
            elif acao_c == '3':
                print(inimigo, 'se defendeu!')
            elif acao_c == '4':
                vida_c = min(max_c, vida_c + 30)
                pocoes_c -= 1
                print(inimigo, 'usou uma poção!')
        rodada += 1

    if fugiu:
        print('Você fugiu!')
        vitorias = 0
    elif vida_c == 0:
        print('Você venceu!')
        vitorias += 1
        if vitorias >= 3 and not evoluiu:
            print(nome, 'evoluiu para', evolucao, '!')
            nome = evolucao
            vida_max += 30
            ataque += 10
            evoluiu = True
    else:
        print('Você perdeu!')
        vitorias = 0
    print('Vitórias consecutivas:', vitorias)
    continuar = input('Jogar novamente? (s/n): ').lower()
    while continuar not in ('s', 'n'):
        continuar = input('Digite s ou n: ').lower()
print('Obrigada por jogar!')
