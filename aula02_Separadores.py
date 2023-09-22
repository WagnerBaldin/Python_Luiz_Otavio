print("-----------------------------")
print(1)
print(2,3) # o python dá um espaço mesmo se não tiver
print(4, 5)
print(56, 78)
print(56, "78") # imprimindo um número e uma string
print("56 78")
print("56", 78)
print("-----------------------------")
# Separador
# O separador é basicamente uma String entre os argumentos
print(12, 34)
print(56, 78, sep='') # retira o espaço
print(56, 78, sep='-') # adiciona o traço no espaço
print(56, 78, sep='~~~~') # aspas simples
print(56, 78, sep="~~~~") # aspas duplas
print(56, 78, sep="texto") #
print(56, 78, sep=" texto ")
print(56, 78, sep="......")
print(56, 78, 9, 10, sep="......")
print(5, 6, 7, 8, 9, 10, sep=" ++++++ ")
print("-----------------------------")
print("Meu nome é Wagner Baldin")
print("-----------------------------")
# LF (Line Feed) e CRLF (Carriage Return + Line Feed) 
# referem-se ao modo pelo qual a linha de texto, do nosso código, 
# é finalizada. Ambos são utilizados para um controle das linhas

# quebra de linhas \n
print(56, 78, 9, 10, sep="......", end='\n1112')
print(1234, end='\n5678')
print("")
print("Meu nome é Wagner", end='\nBaldin')
print('')
print("-----------------------------")
