Opcao1 = 0
Opcao2 = 0

Documento = int(input('''
 1 -  Para RG 
 2 -  Para T�tulo de Eleitor
 
 Digite o tipo de Documento: '''))
 
if Documento == 1:
      Numero = int(input("Digite o n�mero do RG: "))
      if Numero == 12345678:
          print('O eleitor Jo�o do Carmo pode votar!')
      else:
           print('Eleitor n�o encontrado!') 
           
elif Documento == 2:
    Numero = int(input("Digite o n�mero do T�tulo: "))
    if Numero == 11122233344:
          print('O eleitor Jo�o do Carmo pode votar!')
    else:
          print('Eleitor n�o encontrado!')
          
        
Candidato = int(input('''
10 - Paulo Freire
20 - Jean Piaget 

Escolha seu candidato: '''))

if Candidato == 10:
    Opcao1 += 1
    
    print(f'O Candidato Paulo Freire agora possui: {Opcao1}')
    Voto = int(input('Voto feito para Paulo Freire!'))
else:
    Opcao2 += 1
     
    
if Candidato == 20:
    Opcao1 += 1
    
    print(f'O Candidato Jean Piaget possui: {Opcao2}')
    Voto = int(input('Voto feito para Jean Piaget!'))
else:
     print('candidato n�o encontrado!')
     
    
     

     
  

          