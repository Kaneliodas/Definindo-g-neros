#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
gen = input("Qual o seu gênero? Digite F para Feminino e M para Masculino.")
if (gen == 'F'):
    print("Então você é do gênero Feminino.")
if (gen == 'M'):
     print("Então você é do gênero Masculino.")
else:
    print("gênero indefinido.")
