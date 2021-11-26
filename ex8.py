media = int(input(" Digite a sua média de 0 a 10: "))
frequencia = int(input(" Digite a sua frequência de 0 a 100: "))

if frequencia < 75: 
   print("Você foi reprovado(a)")
elif frequencia > 75 and media >= 7: 
   print("Você foi aprovado(a)")
if frequencia > 75 and media < 7 : 
   print("Você está de recuperação")


    


