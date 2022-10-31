Documento = int(input('''
 1 -  Para RG 
 2 -  Para Título de Eleitor
 
 Digite o tipo de Documento: '''))
 
if Documento == 1:
      Numero = int(input("Digite o número do RG: "))
      if Numero == 12345678:
          print('O eleitor João do Carmo pode votar!')
      else:
           print('Eleitor não encontrado!') 
           
elif Documento == 2:
    Numero = int(input("Digite o número do Título: "))
    if Numero == 11122233344:
          print('O eleitor João do Carmo pode votar!')
    else:
          print('Eleitor não encontrado!')
          
           