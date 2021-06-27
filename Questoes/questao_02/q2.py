# Abre o arquivo txt "pib_municipio_2010_a_2018" para utilização no código
arq = open('../dataset/pib_municipio_2010_a_2018.txt','r', encoding='utf-8')

# Definições de variáveis que serão utilizadas no código
contadorLinhas = 0
contadorLinhasSomaPIB = 0
somaPIB = 0
mediaPIB = 0
listaCalculo = []

arq.readline() # Pula para a linha seguinte, já que a primeira linha é somente os nomes das 'colunas'


for linha in arq: # Abre um for para ler todas as linhas do arquivo
    linha = linha.rstrip() # Retira o espaço do início e do fim da linha
    dados = linha.split(';') # Separa as partes da linha em uma lista
    padrao = [dados[1], dados[13], 1] # Cria um padrão de lista para ser preenchido com dados de cada linha lida
    estadoInserido = False # Atribui a booleana estadoInserido como false
        
    if len(listaCalculo) == 0: # Se a listaCalculo estiver vazia, faça:
        listaCalculo.append(padrao) # Acrescente o padrão dentro de listaCalculo
    else:
        if int(dados[0]) == 2010: # Se a linha for de 2010, faça:
            for i in range (len(listaCalculo)): # Preenche o 'i' com o range do tamanho da listaCalculo
                if dados[1] in listaCalculo[i][0]: # Se o estado da linha já estiver preenchido dentro de listaCalculo
                    toInt = int(float(listaCalculo[i][1])) + int(float(dados[13])) # Faz a soma dos valores da listaCalculo + linha lida
                    listaCalculo[i][1] = toInt # Preenche a listaCalculo com a soma
                    listaCalculo[i][2] += 1 # Acrescenta uma variável na counter
                    estadoInserido = True # Atribui a booleana como True

            if estadoInserido == False: # Se o estado não estiver inserido na lista, faça:
                listaCalculo.append(padrao) # Acrescente o padrão dentro de listaCalculo

for mediaPIB in listaCalculo: # Abre um for para ler todos os dados de listaCalculo
    somaPIB = float(mediaPIB[1]) # Transforma a mediaPIB para float
    contadorLinhasSomaPIB = int(mediaPIB[2]) # Transforma a contadorLinhasSomaPIB para float
    mediaPIB[1] = somaPIB / contadorLinhasSomaPIB # Faz o calculo do PIB e acrescenta na lista mediaPIB
    mediaPIB.pop() # Descarta o último elemento da lista mediaPIB

def get_key_mediaPIB(c): # Função que retorna a key com mediaPIB
      return c[1]

#Ordena a listaCalculo de forma ordenada, seguindo do maior PIB para o menor PIB
listaCalculoOrdenada = sorted(listaCalculo, key = get_key_mediaPIB, reverse=True)

result = open("saida_q2.txt",'w', encoding='utf-8') # Cria um arquivo com a saida_q2.txt

for h in range(len(listaCalculoOrdenada)): # Abre um for para ler todos os dados de listaCalculoOrdenada
    print(h , listaCalculoOrdenada[h][0])
    result.write("Lugar no Ranking: ")
    result.write(str(h+1))
    result.write(" | Estado: ")     # Preenche dados dentro do arquivo result
    result.write(listaCalculoOrdenada[h][0])
    result.write(" | Média do PIB per Capita: ")
    result.write(str(listaCalculoOrdenada[h][1]))
    result.write("\n")

result.close()
arq.close() # Encerra arquivos
