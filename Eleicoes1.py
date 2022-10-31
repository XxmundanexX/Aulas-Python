RG = 1
Titulo = 2
documento = int(input('''1 - para RG 
2 - para titulo de eleitor 
Digite o tipo de Documento aqui: '''))
if RG == 1:
    numero = int(input("Digite aqui o Número do RG: "))
    if numero == 12345678:
        print(" Eleitor João de Carmo. PODE VOTAR!")
    else:
        print("Eleitor não encontrado")

if documento == 2:
    titulo = int(input('Digite o número do Título:'))
    if titulo == 11122233344:
        print('Pode Votar!')
        print('João do Carmo')
    else:
        print('Eleitor não encontrado')