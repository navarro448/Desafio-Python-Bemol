# Abre o arquivo txt "pib_municipio_2010_a_2018" para utilização no código
arq = open('../dataset/pib_municipio_2010_a_2018.txt','r', encoding='utf-8')


# Definições de variáveis que serão utilizadas no código
contadorLinhasSomaPIB = 0
somaPIB = 0
mediaPIB = 0

arq.readline() # Pula para a linha seguinte, já que a primeira linha é somente os nomes das 'colunas'

for linha in arq: # Abre um for para ler todas as linhas do arquivo
    linha = linha.rstrip() # Retira o espaço do início e do fim da linha

    if 'Manaus' in linha:  # Se em alguma dessas linhas possuir a palavra 'Manaus', então:
        dados = linha.split(';') # Separa as partes da linha em uma lista
        print("PIB da linha encontrada:", dados[13]) # Printa o PIB encontrado da linha 
        somaPIB = somaPIB + float(dados[13]) # Acrescenta esse valor em somaPIB
        contadorLinhasSomaPIB = contadorLinhasSomaPIB + 1 # Soma +1 no contador de Linhas que foram lidas

                
mediaPIB = somaPIB / contadorLinhasSomaPIB # Faz o cálculo para receber a media do PIB Total
arq.close() # Fecha o arquivo

result = open("saida_q1.txt",'w', encoding='utf-8') # Cria um arquivo com a saida_q1.txt
# Escreve as informações necessárias dentro desse arquivo
result.write("Foram retornadas ")
result.write(str(contadorLinhasSomaPIB))
result.write(" linhas do arquivo com os dados de Manaus \nSoma total do PIB: ")
result.write(str(somaPIB)) # Preenche essa saída com os dados
result.write("\nMédia do PIB per Capita em Manaus: ")
result.write(str(mediaPIB))
result.write("\nobs: *Produto Interno Bruto per capita a preços correntes (R$ 1,00)*")
result.close() # Fecha esse arquivo
