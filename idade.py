idade = int(input("digite sua idade aqui: "))
if idade < 12:
    print("crian�a")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")