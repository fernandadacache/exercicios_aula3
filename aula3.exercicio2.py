#exercicio 2

dicionario = {1 : "Seg" , 2 : "Ter" , 3 : "Qua" , 4 : "Qui" , 5 : "Sex" , 6 : "Sab" , 7 : "Dom"}
numero = int(input("Digite um numero:"))
if numero >=1 and numero <=7 :
    print("O dia da semana é:" , dicionario[numero])
else:
   print ("Escolha um numero de 1 a 7")
    



