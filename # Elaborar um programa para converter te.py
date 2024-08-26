# Elaborar um programa para converter temperaturas
# O menu deverá ter as seguintes opções: "no caderno"

#cf = t*1.8 + 32
#ck = t + 273
#fk = t + 459.67*5/9
#kc = t - 273

print("1 : De grau celsius para fahrenheit")
print("2 : De grau celsius para kelvin")
print("3 : De grau fahrenheit para kelvin")
print("4 : De grau kelvin para celsius")
o = float(input("Digite sua opção de conversão(1,2,3,4): "))



if o == "1":
    t = int(input("Digite o número da temperatura: "))
    f = (t * 1.8) + 32
    print(str(f))

elif o == "2":
    totall = (t + 273)
    print(str(totall))

elif o == "3":
    totalll = (t + 459.67*5/9)
    print(str(totalll))