"""
Proposito:
    Script para auxiliar a criação do 'requirements.txt' com o 'Poetry'.
    Ao rodar o 'Poetry export --without-hashs' para exportar o 'requirements.txt',
    ele vem com informações que não são necessárias. Este script remove essas informações desnecessárias.
"""

import re


# Abre o arquivo 'requirements.txt' no modo de leitura e escrita ('r+').
with open("requirements.txt", "r+") as file:
    # Lê todas as linhas do arquivo 'requirements.txt' e as armazena na variável 'lines'.
    lines = file.readlines()

    # Utiliza uma compreensão de lista para remover tudo após o caractere ';' em cada linha.
    # A função 're.sub' substitui a parte da string que corresponde à expressão regular por uma string vazia.
    # O método 'strip' é usado para remover espaços em branco no início e no fim de cada linha.
    data = [re.sub(r";.*", "", line).strip() for line in lines]

    # Move o ponteiro do arquivo para o início, efetivamente apagando o conteúdo anterior.
    file.seek(0)
    # Trunca o arquivo para o tamanho atual do ponteiro, garantindo que o conteúdo anterior seja removido.
    file.truncate()

    # Escreve as linhas modificadas de volta ao arquivo 'requirements.txt', adicionando uma nova linha após cada uma.
    for line in data:
        file.write(line + "\n")
