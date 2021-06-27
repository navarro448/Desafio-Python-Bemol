# Abre o arquivo txt "pib_municipio_2010_a_2018" para utilização no código
arq = open('../dataset/pib_municipio_2010_a_2018.txt','r', encoding='utf-8')

# Definições de variáveis que serão utilizadas no código
somaVssTotal2018 = 0;
counterVssTotal2018 = 0;
mediaVssTotal2018 = 0;
somaVssAM2018 = 0;
counterVssAM2018 = 0;
mediaVssAM2018 = 0;

arq.readline() # Pula para a linha seguinte, já que a primeira linha é somente os nomes das 'colunas'


for linha in arq: # Abre um for para ler todas as linhas do arquivo
    linha = linha.rstrip() # Retira o espaço do início e do fim da linha
    dados = linha.split(';') # Separa as partes da linha em uma lista
    
    if int(dados[0]) == 2018: # Se o ano da linha lida for 2018, faça:
        somaVssTotal2018 += int(dados[8]) # Soma os dados de VSS da linha e armazena na variável
        counterVssTotal2018 += 1 # Soma o count de quantas linhas foram lidas
        
        if dados[1] == 'AM': # Se esses dados de 2018 forem do estado AM, faça:
            somaVssAM2018 += int(dados[8]) # Soma os dados de VSS da linha e armazena na variável
            counterVssAM2018 += 1 # Soma o count de quantas linhas foram lidas


# Deixa vísivel todos os dados e calculos feitos para preenchimento das Somas, Counters e Médias + relação
print(somaVssTotal2018)
print(counterVssTotal2018)
mediaVssTotal2018 = somaVssTotal2018 / counterVssTotal2018
print("media do VSS total de 2018:", mediaVssTotal2018)

print(somaVssAM2018)
print(counterVssAM2018)
mediaVssAM2018 = somaVssAM2018 / counterVssAM2018
print("media do VSS de AM em 2018: ", mediaVssAM2018)

relacao = mediaVssTotal2018 / mediaVssAM2018
print("relação da media total sobre a media de Manaus, no mesmo periodo: ", relacao)

arq.close() # Fecha o arquivo



result = open("saida_q3.txt",'w', encoding='utf-8') # Cria um arquivo com a saida_q3.txt
result.write("Média do Valor adicionado bruto dos Serviços Total de 2018 em todos os estados: ")
result.write(str(mediaVssTotal2018))
result.write("\nMédia do Valor adicionado bruto dos Serviços Total de 2018 no estado de Manaus: ")
result.write(str(mediaVssAM2018))# Preenche dados dentro do arquivo result
result.write("\nRelação entre a média do Valor adicionado bruto dos Serviços Total de todos os estados em comparação a média de Manaus em 2018: ")
result.write(str(relacao))
result.close() # Encerra arquivos
