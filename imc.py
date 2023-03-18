p = float(input("Informe o peso: "))
a = float(input("Informe a altura: "))

imc = p/(a*a) 
if(imc < 18.5):
    print("Magreza, imc é:" + str(imc) )
   
elif(imc >= 18.5 and imc<= 24.9):
    print("Normal, imc é:"+ str(imc))

elif(imc >= 25 and imc <= 29.9):
    print("Sobre peso, imc é:"+ str(imc))

elif(imc >= 30 and imc <= 34.9):
    print("Obesidade grau I, imc é:"+ str(imc))

elif(imc >= 35 and imc <= 39.9):
    print("Obesidade grau II, imc é:"+ str(imc))

else:
    print("Obesidade grau III, imc é:"+ str(imc))