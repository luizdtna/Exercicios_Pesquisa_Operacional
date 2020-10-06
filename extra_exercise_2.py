matriz = []

file = open('matriz4', 'r')
for i in file:
    i = i.replace('\n', '')
    i = i.split(' ')
    matriz.append(i)
file.close()

row_col = len(matriz[0])  # numero de linhas/colunas


def exercise_A():
    print('Exercicio escolhido: A')
    print('________')
    cidade = input('Digite o número da cidade de 0 à ' + str(row_col - 1) + ': ')
    chegam = 0
    saem = 0
    for i in range(row_col):

        for j in range(row_col):
            if j == int(cidade) and j != i and (matriz[i][j]) == '1':
                chegam += 1
            if i == int(cidade) and j != i and (matriz[i][j]) == '1':
                saem += 1
    return str(saem) + ' estradas saem da cidade' + '\n' + str(chegam) + ' estradas chegam até a cidade'


def exercise_B():
    print('Exercicio escolhido: B')
    print('________')

    bigger_now = 0
    records = {'bigger': [], 'arrives': 0}

    for i in range(row_col):
        for j in range(row_col):
            if matriz[j][i] == '1':  # Vou analisar por coluna, e não pela linha
                bigger_now += 1

        if bigger_now > records['arrives']:
            records['bigger'].clear()  # Como esta agr é a cidade que mais recebe,
            # retira as outras cidades do vetor
            records['bigger'].append(i)  # Add a cidade como a que mais recebe rodovias
            records['arrives'] = bigger_now  # add o numero de rodovias

        elif bigger_now == records['arrives']:
            records['bigger'].append(i)  # Se as cidades recebem o mesmo tanto de rodovias
            records['arrives'] = bigger_now
        bigger_now = 0

    records['arrives'] -= 1  # Retira a cidade atual da contagem
    return 'Nas cidades ' + str(records['bigger']) + ' chegam o maior numero de rodovias: ' + str(records['arrives'])


def exercise_C():
    print('Exercicio escolhido: C')
    print('________')
    mao_dupla = []
    cidade = int(input('Digite o número da cidade de 0 à ' + str(row_col - 1) + ': '))

    for j in range(row_col):
        if matriz[cidade][j] == '1':
            if matriz[j][cidade] == '1' and cidade != j:
                mao_dupla.append(j)
    return 'Tem mão dupla com as cidades: ' + str(mao_dupla)


def exercise_D():
    print('Exercicio escolhido: D')
    print('________')
    saida_direta = []
    cidade = int(input('Digite o número da cidade de 0 à ' + str(row_col - 1) + ': '))
    for j in range(row_col):
        if matriz[j][cidade] == '1' and j != cidade:  # Vou analisar por coluna, e não pela linha
            saida_direta.append(j)
    return saida_direta


def exercise_F():
    print('Exercicio escolhido: F')
    print('________')
    roteiro = input('Digite o roteiro entre as cidades de 0 à ' + str(row_col - 1) + '. Exemplo: 2 3 2 1 0: ')
    roteiro = roteiro.split(' ')

    vetor = []
    vetor.append(roteiro[0])

    for i in range(len(roteiro) - 1):
        continuation_F(roteiro[i + 1], roteiro[i], vetor)

    if vetor == roteiro:
        return 'Existe caminho'
    else:
        return 'Não existe caminho'


def continuation_F(next, atual, vetor):
    next = int(next)
    atual = int(atual)

    if next == atual:  # Chegou na proxima cidade. Kij com i == j
        return

    if matriz[atual][next] == '1':
        vetor.append(str(next))
        continuation_F(next, next, vetor)


def exercise_E():
    print('Exercicio escolhido: E')
    print('________')
    com_saida = 0
    com_entrada = 0
    final = ''

    for i in range(row_col):
        for j in range(row_col):
            if i != j:
                if matriz[i][j] == '1':
                    com_saida += 1
                if matriz[j][i] == '1':
                    com_entrada += 1

        if com_saida == com_entrada == 0:
            final += 'Cidade ' + str(i) + ' é isolada\n'
        elif com_entrada == 0:
            final += 'Cidade ' + str(i) + ' é sem entrada\n'
        elif com_saida == 0:
            final += 'Cidade ' + str(i) + ' é sem saída\n'
    if final == '':
        final += 'Não existe cidades que atendam aos critérios I II e III'
    return final

op = int(input('Digite o código de acordo com exercicio: \n'
               '0: exercise_A(), \n'
               '1: exercise_B(), \n'
               '2: exercise_C(), \n'
               '3: exercise_D(), \n'
               '4: exercise_E(), \n'
               '5: exercise_F(), \n'
               '>>'))
if op == 0:
    print(exercise_A())
elif op == 1:
    print(exercise_B())
elif op == 2:
    print(exercise_C())
elif op == 3:
    print(exercise_D())
elif op == 4:
    print(exercise_E())
elif op == 5:
    print(exercise_F())
